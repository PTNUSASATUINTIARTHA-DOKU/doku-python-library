class UpdateVAConfig:

    def __init__(self, status: str):
        self.status = status
    
    def create_request_body(self) -> dict:
        return {
            "status": self.status
        }