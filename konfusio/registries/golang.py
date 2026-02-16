import requests

def exists(pkg):
    url = f"https://proxy.golang.org/{pkg}/@v/list"
    r = requests.get(url, timeout=5)
    return r.status_code == 200
