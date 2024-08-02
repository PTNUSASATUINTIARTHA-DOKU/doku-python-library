
class PaymentNotificationResponseHeader:

    def __init__(self, xTimestamp: str) -> None:
        self.x_timestamp = xTimestamp
        self.content_type = "application/json"