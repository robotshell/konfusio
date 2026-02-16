_registry_cache = {}

def get_cached(pkg, ecosystem):
    return _registry_cache.get((pkg, ecosystem))

def set_cache(pkg, ecosystem, value):
    _registry_cache[(pkg, ecosystem)] = value
