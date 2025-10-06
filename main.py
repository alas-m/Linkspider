from spider.crawler import crawl_site
from spider.visualizer import draw_graph
import argparse
import logging
import sys
import json
import signal
from urllib.parse import urlparse
import networkx as nx
from utils.url_utils import get_domain

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def is_valid_url(url):
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False

def save_graph_data(graph, output_json):
    if graph is None:
        logging.error("Graph is None - nothing to save")
        return False
        
    if len(graph.nodes) == 0:
        logging.warning("Graph has 0 nodes - nothing to save")
        return False
        
    graph_data = {
        "nodes": list(graph.nodes()),
        "edges": list(graph.edges()),
        "stats": {
            "total_nodes": len(graph.nodes),
            "total_edges": len(graph.edges)
        }
    }
    
    try:
        with open(output_json, 'w', encoding='utf-8') as f:
            json.dump(graph_data, f, indent=2, ensure_ascii=False)
        
        logging.info(f"Graph data saved to {output_json}")
        return True
    except Exception as e:
        logging.error(f"Failed to save JSON: {e}")
        return False

class CrawlManager:
    def __init__(self, url, depth, png_output):
        self.url = url
        self.depth = depth
        self.png_output = png_output
        self.json_output = f"{get_domain(url).replace('.', '_')}_graph.json"
        self.graph = None
        
    def handle_interrupt(self, sig, frame):
        logging.info("Crawl interrupted by user - saving current progress...")
        self.save_progress()
        sys.exit(0)
        
    def save_progress(self):
        if self.graph is not None:
            logging.info(f"Attempting to save graph with {len(self.graph.nodes)} nodes and {len(self.graph.edges)} edges")
            
            try:
                if len(self.graph.nodes) > 0:
                    draw_graph(self.graph, output_file=self.png_output)
                    logging.info(f"Graph image saved to {self.png_output}")
                else:
                    logging.warning("No nodes to visualize")
                
                if save_graph_data(self.graph, self.json_output):
                    logging.info("Progress saved successfully")
                    logging.info("Program is finished. CR: alas-m")
                else:
                    logging.error("Failed to save progress")
                    
            except Exception as e:
                logging.error(f"Error during save: {e}")
        else:
            logging.error("No graph object exists to save")
            
    def run(self):
        signal.signal(signal.SIGINT, self.handle_interrupt)
        
        try:
            logging.info(f"Starting crawl of {self.url} with depth {self.depth}")
            self.graph = crawl_site(self.url, self.depth)
            
            logging.info(f"Crawl finished. Graph stats: {len(self.graph.nodes)} nodes, {len(self.graph.edges)} edges")
            
            self.save_progress()
            
        except Exception as e:
            logging.error(f"Execution error: {str(e)}")
            self.save_progress()
            sys.exit(1)

def main():
    parser = argparse.ArgumentParser(description="LinkSpider: website analyzer")
    parser.add_argument("--url", required=True, help="Starting URL")
    parser.add_argument("--depth", type=int, default=2, help="Crawl depth (1-5)")
    parser.add_argument("--output", default="graph.png", help="Output PNG file")
    
    args = parser.parse_args()

    if not is_valid_url(args.url):
        logging.error(f"Invalid URL: {args.url}")
        sys.exit(1)
        
    if args.depth < 1 or args.depth > 5:
        logging.error("Crawl depth must be between 1 and 5")
        sys.exit(1)

    manager = CrawlManager(args.url, args.depth, args.output)
    manager.run()

if __name__ == "__main__":
    main()