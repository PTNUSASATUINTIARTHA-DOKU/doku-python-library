from doku_python_library.src.model.va.origin import Origin
class PaymentJumpAppAdditionalInfo:

    def __init__(self, channel: str, order_title: str = None, metadata: str = None) -> None:
        self.channel = channel
        self.order_title = order_title
        self.metadata = metadata
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "metadata": self.metadata,
            "origin": Origin.create_request_body()
        }