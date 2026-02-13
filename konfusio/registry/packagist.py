import requests
from .base import BaseRegistry

class PackagistRegistry(BaseRegistry):
    name = "packagist"

    def exists(self, package):
        try:
            url = f"https://repo.packagist.org/p2/{package}.json"
            r = requests.get(url, timeout=5)
            return r.status_code != 404
        except:
            return True
