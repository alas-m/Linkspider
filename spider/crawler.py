import requests
import networkx as nx
from spider.parser import extract_links
from utils.url_utils import normalize_url, get_domain
import time

def crawl_site(start_url, max_depth=2):
    graph = nx.DiGraph()
    visited = set()
    to_visit = [(start_url, 0)]
    domain = get_domain(start_url)
    
    graph.add_node(start_url)
    
    try:
        while to_visit:
            current_url, depth = to_visit.pop(0)
            
            if current_url in visited:
                continue
                
            visited.add(current_url)
            
            try:
                print(f"[+] Crawling: {current_url} (depth {depth})")
                response = requests.get(current_url, timeout=10)
                
                if response.status_code == 200:
                    links = extract_links(response.text, current_url)
                    print(f"    Found {len(links)} links")
                    
                    for link in links:
                        normalized_link = normalize_url(link, current_url)
                        
                        if get_domain(normalized_link) == domain:
                            graph.add_node(normalized_link)
                            graph.add_edge(current_url, normalized_link)
                            
                            if depth < max_depth and normalized_link not in visited:
                                to_visit.append((normalized_link, depth + 1))
                    
                    time.sleep(0.2)
                else:
                    print(f"[-] HTTP {response.status_code} for {current_url}")
                    
            except Exception as e:
                print(f"[-] Failed to crawl {current_url}: {e}")
                continue

        print(f"\n[✓] Crawling complete. Graph has {len(graph.nodes)} nodes and {len(graph.edges)} edges")
        
    except KeyboardInterrupt:
        print(f"\n[!] Crawling interrupted. Current progress: {len(graph.nodes)} nodes, {len(graph.edges)} edges")
    
    return graph
