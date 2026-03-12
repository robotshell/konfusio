import requests

def exists(pkg):
    url = f"https://pypi.org/pypi/{pkg}/json"
    try:
        r = requests.get(url, timeout=5)
        return r.status_code == 200
    except requests.exceptions.RequestException:
        return False
