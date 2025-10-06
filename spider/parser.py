from bs4 import BeautifulSoup
from utils.url_utils import normalize_url

def extract_links(html_content, base_url):
    soup = BeautifulSoup(html_content, 'html.parser')
    links = set()
    
    for tag in soup.find_all("a", href=True):
        href = tag.get("href")
        if href and not href.startswith(('javascript:', 'mailto:', '#')):
            normalized_url = normalize_url(href, base_url)
            links.add(normalized_url)
    
    return list(links)