from konfusio.registries import npm, pypi, packagist, maven, golang, rubygems, nuget

def check_registry(pkg, ecosystem):
    if ecosystem == "npm":
        return npm.exists(pkg)
    if ecosystem == "pypi":
        return pypi.exists(pkg)
    if ecosystem == "packagist":
        return packagist.exists(pkg)
    if ecosystem == "maven":
        return maven.exists(pkg)
    if ecosystem == "golang":
        return golang.exists(pkg)
    if ecosystem == "rubygems":
        return rubygems.exists(pkg)
    if ecosystem == "nuget":
        return nuget.exists(pkg)

    return True
