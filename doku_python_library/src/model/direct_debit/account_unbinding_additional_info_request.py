from doku_python_library.src.model.va.origin import Origin
class AccountUnbindingAdditionalInfoRequest:

    def __init__(self, channel: str) -> None:
        self.channel = channel
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "origin": Origin.create_request_body()
        }