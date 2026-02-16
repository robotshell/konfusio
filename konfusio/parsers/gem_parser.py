import re

def parse_gemfile(content):
    matches = re.findall(r"gem ['\"](.*?)['\"]", content)
    return set(matches)
