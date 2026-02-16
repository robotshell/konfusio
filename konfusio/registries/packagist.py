import requests

def exists(pkg):
    url = f"https://repo.packagist.org/p2/{pkg}.json"
    r = requests.get(url, timeout=5)
    return r.status_code == 200
