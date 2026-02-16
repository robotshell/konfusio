import requests

def fetch(url):
    try:
        r = requests.get(url, timeout=10)
        return r.text
    except:
        return ""
