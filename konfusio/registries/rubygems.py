import requests

def exists(pkg):
    url = f"https://rubygems.org/api/v1/gems/{pkg}.json"
    r = requests.get(url, timeout=5)
    return r.status_code == 200
