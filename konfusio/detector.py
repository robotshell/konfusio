from konfusio.parsers.js_parser import parse_js
from konfusio.parsers.npm_parser import parse_npm_manifest
from konfusio.parsers.composer_parser import parse_composer
from konfusio.parsers.requirements_parser import parse_requirements
from konfusio.parsers.maven_parser import parse_maven
from konfusio.parsers.go_parser import parse_go_mod
from konfusio.parsers.gem_parser import parse_gemfile


def detect_ecosystem(url, content):

    if url.endswith(".js"):
        return "npm", parse_js

    if url.endswith("package.json") or url.endswith("package-lock.json"):
        return "npm", parse_npm_manifest

    if url.endswith("composer.json"):
        return "packagist", parse_composer

    if url.endswith("requirements.txt"):
        return "pypi", parse_requirements

    if url.endswith("pom.xml"):
        return "maven", parse_maven

    if url.endswith("go.mod"):
        return "golang", parse_go_mod

    if url.endswith("Gemfile"):
        return "rubygems", parse_gemfile

    return None, None
