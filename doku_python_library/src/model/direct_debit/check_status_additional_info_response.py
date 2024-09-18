
class CheckStatusAdditionalInfoResponse:

    def __init__(self, deviceId: str = None, channel: str = None, acquirer = None) -> None:
        self.device_id = deviceId
        self.channel = channel
        self.acquirer = acquirer