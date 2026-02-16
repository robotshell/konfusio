import requests

def exists(pkg):
    url = f"https://registry.npmjs.org/{pkg}"
    r = requests.get(url, timeout=5)
    return r.status_code == 200
