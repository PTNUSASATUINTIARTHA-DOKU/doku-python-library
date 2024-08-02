class DeleteVAAdditionalInfo:

    def __init__(self, channel: str) -> None:
        self.channel = channel
    
    def json(self) -> dict:
        return {
            "channel": self.channel
        }