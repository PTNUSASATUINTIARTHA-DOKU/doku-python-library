class UrlParam:

    def __init__(self, url: str, type: str, is_deep_link: str) -> None:
        self.url = url
        self.type = type
        self.is_deep_link = is_deep_link
    
    def json(self) -> dict:
        return {
            "url": self.url,
            "type": self.type,
            "isDeepLink": self.is_deep_link
        }
