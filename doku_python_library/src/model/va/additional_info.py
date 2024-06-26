class AdditionalInfo:

    def __init__(self, channel: str, reusable: bool = False) -> None:
        self.channel = channel
        self.reusable = reusable
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "reusable": self.reusable
        }