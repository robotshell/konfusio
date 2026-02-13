import requests
from .base import BaseRegistry

class NuGetRegistry(BaseRegistry):
    name = "nuget"

    def exists(self, package):
        try:
            url = f"https://api.nuget.org/v3-flatcontainer/{package}/index.json"
            r = requests.get(url, timeout=5)
            return r.status_code != 404
        except:
            return True
