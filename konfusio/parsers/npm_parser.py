import json

def parse_npm_manifest(content):
    try:
        data = json.loads(content)
    except:
        return set()

    packages = set()

    for key in ["dependencies", "devDependencies"]:
        if key in data:
            packages.update(data[key].keys())

    return packages
