import json

def parse_composer(content):
    try:
        data = json.loads(content)
    except:
        return set()

    packages = set()

    if "require" in data:
        packages.update(data["require"].keys())

    if "require-dev" in data:
        packages.update(data["require-dev"].keys())

    return packages
