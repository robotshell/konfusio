from konfusio.parsers import npm, composer, pypi, maven, golang, rubygems, nuget

def detect_ecosystem(url, content):
    if url.endswith("package.json"):
        return "npm", npm.parse_package_json

    if url.endswith("package-lock.json"):
        return "npm", npm.parse_package_lock

    if url.endswith("composer.json"):
        return "packagist", composer.parse_composer

    if url.endswith("requirements.txt"):
        return "pypi", pypi.parse_requirements

    if url.endswith("pom.xml"):
        return "maven", maven.parse_pom

    if url.endswith("go.mod"):
        return "golang", golang.parse_go_mod

    if url.endswith("Gemfile"):
        return "rubygems", rubygems.parse_gemfile

    if url.endswith(".csproj"):
        return "nuget", nuget.parse_csproj

    if url.endswith(".js"):
        return "npm", npm.parse_js

    return None, None
