import requests
from .base import BaseRegistry

class GoRegistry(BaseRegistry):
    name = "golang"

    def exists(self, package):
        try:
            url = f"https://proxy.golang.org/{package}/@v/list"
            r = requests.get(url, timeout=5)
            return r.status_code != 404 and bool(r.text.strip())
        except:
            return True
