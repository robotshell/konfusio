import json
import re

def parse_package_json(content):
    data = json.loads(content)
    deps = data.get("dependencies", {})
    return list(deps.keys())

def parse_package_lock(content):
    data = json.loads(content)
    deps = data.get("dependencies", {})
    return list(deps.keys())

def parse_js(content):
    pattern = r'["\'](@?[a-zA-Z0-9_\-/]+)["\']'
    matches = re.findall(pattern, content)
    return list(set(matches))
