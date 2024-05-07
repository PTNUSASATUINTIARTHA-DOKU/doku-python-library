class TotalAmount:

    def __init__(self, value: str, currency: str) -> None:
        self.value = value
        self.currency = currency
    
    def json(self) -> dict:
        return {
            "value": self.value,
            "currency": self.currency
        }