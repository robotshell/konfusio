import requests
from .base import BaseRegistry

class PyPIRegistry(BaseRegistry):
    name = "pypi"

    def exists(self, package):
        try:
            r = requests.get(f"https://pypi.org/pypi/{package}/json", timeout=5)
            return r.status_code != 404
        except:
            return True
