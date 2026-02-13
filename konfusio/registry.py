import requests

NPM_REGISTRY = "https://registry.npmjs.org/"
_cache = {}

def check_package(package):
    if package in _cache:
        return _cache[package]

    try:
        r = requests.get(NPM_REGISTRY + package, timeout=5)
        exists = r.status_code != 404
    except:
        exists = True

    _cache[package] = exists
    return exists
