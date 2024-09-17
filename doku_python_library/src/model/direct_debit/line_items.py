class LineItems:

    def __init__(self, name: str, price: str, quantity: str) -> None:
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def json(self) -> dict:
        return {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity
        }