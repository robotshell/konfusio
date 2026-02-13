class BaseRegistry:
    name = "base"

    def exists(self, package: str) -> bool:
        raise NotImplementedError
