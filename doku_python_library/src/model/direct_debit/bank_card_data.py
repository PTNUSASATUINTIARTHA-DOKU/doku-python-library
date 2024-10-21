class BankCardData:
    
    def __init__(self, bank_card_no: str, bank_card_type: str, expiry_date: str) -> None:
        self.bank_card_no = bank_card_no
        self.bank_card_type = bank_card_type
        self.expiry_date = expiry_date
    
    def json(self) -> dict:
        return {
            "bankCardNo": self.bank_card_no,
            "bankCardType": self.bank_card_type,
            "expiryDate": self.expiry_date
        }