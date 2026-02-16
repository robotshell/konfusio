class BaseRegistry:
    name = "base"

    def exists(self, package: str) -> bool:
        """Return True if the package exists in the registry"""
        raise NotImplementedError
