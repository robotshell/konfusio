import requests

def exists(pkg):
    try:
        r = requests.get(f"https://registry.npmjs.org/{pkg}", timeout=5)
        return r.status_code != 404
    except:
        return True
