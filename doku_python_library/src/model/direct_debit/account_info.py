from doku_python_library.src.model.va.total_amount import TotalAmount

class AccountInfo:

    def __init__(self, balance_type: str, amount: TotalAmount, flat_amount: TotalAmount, hold_amount: TotalAmount) -> None:
        self.balance_type = balance_type
        self.amount = amount
        self.flat_amount = flat_amount
        self.hold_amount = hold_amount
    
    def json(self) -> dict:
        return {
            "balanceType": self.balance_type,
            "amount": self.amount.json(),
            "flatAmount": self.flat_amount.json(),
            "holdAmount": self.hold_amount.json()
        }