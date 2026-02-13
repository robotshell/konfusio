import requests

NPM_REGISTRY = "https://registry.npmjs.org/"

def check_package(package):
    try:
        r = requests.get(NPM_REGISTRY + package, timeout=5)
        return r.status_code != 404
    except:
        return True
