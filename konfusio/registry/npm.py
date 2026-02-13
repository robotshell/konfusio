import requests
from .base import BaseRegistry

class NPMRegistry(BaseRegistry):
    name = "npm"

    def exists(self, package):
        try:
            r = requests.get(f"https://registry.npmjs.org/{package}", timeout=5)
            return r.status_code != 404
        except:
            return True
