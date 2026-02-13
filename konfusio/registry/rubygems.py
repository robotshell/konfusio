import requests
from .base import BaseRegistry

class RubyGemsRegistry(BaseRegistry):
    name = "rubygems"

    def exists(self, package):
        try:
            r = requests.get(f"https://rubygems.org/api/v1/gems/{package}.json", timeout=5)
            return r.status_code != 404
        except:
            return True
