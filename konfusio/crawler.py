from urllib.parse import urljoin, urlparse
import requests
from bs4 import BeautifulSoup

KNOWN_MANIFESTS = [
    "package.json",
    "package-lock.json",
    "composer.json",
    "requirements.txt",
    "pom.xml",
    "go.mod",
    "Gemfile"
]

def crawl(base_url):
    discovered = set()

    try:
        r = requests.get(base_url, timeout=10)
    except:
        return []

    soup = BeautifulSoup(r.text, "html.parser")

    # JS files
    for script in soup.find_all("script"):
        src = script.get("src")
        if src:
            full = urljoin(base_url, src)
            discovered.add(full)

    # Try common manifest paths
    parsed = urlparse(base_url)
    root = f"{parsed.scheme}://{parsed.netloc}/"

    for manifest in KNOWN_MANIFESTS:
        discovered.add(urljoin(root, manifest))

    return list(discovered)
