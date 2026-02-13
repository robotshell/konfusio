import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

def is_js(url):
    return url.lower().endswith(".js")

def crawl_for_js(url, depth=2, visited=None):
    if visited is None:
        visited = set()

    js_files = set()

    if depth == 0 or url in visited:
        return js_files

    visited.add(url)

    try:
        r = requests.get(url, timeout=10)
        if "text/html" not in r.headers.get("Content-Type", ""):
            return js_files
    except:
        return js_files

    soup = BeautifulSoup(r.text, "html.parser")

    for script in soup.find_all("script", src=True):
        js_url = urljoin(url, script["src"])
        js_files.add(js_url)

    for link in soup.find_all("a", href=True):
        next_url = urljoin(url, link["href"])
        if urlparse(next_url).netloc == urlparse(url).netloc:
            js_files.update(crawl_for_js(next_url, depth-1, visited))

    return js_files
