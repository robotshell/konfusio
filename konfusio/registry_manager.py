from konfusio.registries.npm import NPMRegistry
from konfusio.registries.pypi import PyPIRegistry

REGISTRIES = [
    NPMRegistry(),
    PyPIRegistry(),
]

def check_all_registries(package):
    results = {}

    for registry in REGISTRIES:
        exists = registry.exists(package)
        results[registry.name] = exists

    return results
