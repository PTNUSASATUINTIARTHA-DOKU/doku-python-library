from doku_python_library.src.model.va.total_amount import TotalAmount

class PayOptionDetail:

    def __init__(self, pay_method: str, trans_amount: TotalAmount, fee_amount: TotalAmount) -> None:
        self.pay_method = pay_method
        self.trans_amount = trans_amount
        self.fee_amount = fee_amount
    
    def json(self) -> dict:
        return {
            "payMethod": self.pay_method,
            "transAmount": self.trans_amount.json(),
            "feeAmount": self.fee_amount.json()
        }