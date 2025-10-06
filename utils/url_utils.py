from urllib.parse import urlparse, urljoin

def normalize_url(url, base_url):
    if not url.startswith("http"):
        url = urljoin(base_url, url)
    parsed = urlparse(url)
    clean_url = parsed.scheme + "://" + parsed.netloc + parsed.path
    return clean_url.rstrip("/")

def get_domain(url):
    return urlparse(url).netloc
