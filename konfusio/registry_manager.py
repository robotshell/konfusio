from konfusio.registries.npm import NPMRegistry
from konfusio.registries.pypi import PyPIRegistry
from konfusio.registries.maven import MavenRegistry
from konfusio.registries.rubygems import RubyGemsRegistry
from konfusio.registries.packagist import PackagistRegistry
from konfusio.registries.golang import GoRegistry
from konfusio.registries.nuget import NuGetRegistry

# Lista de registries activos
REGISTRIES = [
    NPMRegistry(),
    PyPIRegistry(),
    MavenRegistry(),
    RubyGemsRegistry(),
    PackagistRegistry(),
    GoRegistry(),
    NuGetRegistry()
]

def check_all_registries(package):
    results = {}
    for registry in REGISTRIES:
        results[registry.name] = registry.exists(package)
    return results
