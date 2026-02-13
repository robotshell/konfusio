import requests
from .base import BaseRegistry

class MavenRegistry(BaseRegistry):
    name = "maven"

    def exists(self, package):
        # Maven format: groupId:artifactId → split by ":"
        try:
            if ":" in package:
                groupId, artifactId = package.split(":")[:2]
                query = f'g:"{groupId}"+AND+a:"{artifactId}"'
                url = f'https://search.maven.org/solrsearch/select?q={query}&rows=1&wt=json'
                r = requests.get(url, timeout=5)
                data = r.json()
                return data.get("response", {}).get("numFound", 0) > 0
            return False
        except:
            return True
