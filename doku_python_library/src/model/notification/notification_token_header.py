class NotificationTokenHeader:

    def __init__(self, client_id: str, timestamp: str) -> None:
        self.client_id = client_id
        self.timestamp = timestamp
    
    def json(self) -> dict:
        return {
            "x-client-key": self.client_id,
            "x-timestamp": self.timestamp
        }