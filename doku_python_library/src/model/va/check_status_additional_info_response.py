class CheckStatusAdditionalInfoResponse:

    def __init__(self, acquirer: str):
        self.acquirer = acquirer
    
    def json(self) -> dict:
        return {
            "acquirer": self.acquirer
        }