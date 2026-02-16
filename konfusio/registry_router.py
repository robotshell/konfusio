from konfusio.registries import npm, pypi, packagist, maven, golang, rubygems
from konfusio.cache import get_cached, set_cache

def check_registry(pkg, ecosystem):
    cached = get_cached(pkg, ecosystem)
    if cached is not None:
        return cached

    if ecosystem == "npm":
        result = npm.exists(pkg)
    elif ecosystem == "pypi":
        result = pypi.exists(pkg)
    elif ecosystem == "packagist":
        result = packagist.exists(pkg)
    elif ecosystem == "maven":
        result = maven.exists(pkg)
    elif ecosystem == "golang":
        result = golang.exists(pkg)
    elif ecosystem == "rubygems":
        result = rubygems.exists(pkg)
    else:
        result = True

    set_cache(pkg, ecosystem, result)
    return result
