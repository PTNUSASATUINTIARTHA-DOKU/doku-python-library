class BankCardData:
    
    def __init__(self, bank_card_no, bank_card_type, expiry_date, identification_no=None, identification_type=None, email=None):
        self.bankCardNo = bank_card_no
        self.bankCardType = bank_card_type
        self.identificationNo = identification_no
        self.identificationType = identification_type
        self.email = email
        self.expiryDate = expiry_date

    def json(self):
        return {
            "bankCardNo": self.bankCardNo,
            "bankCardType": self.bankCardType,
            "identificationNo": self.identificationNo,
            "identificationType": self.identificationType,
            "email": self.email,
            "expiryDate": self.expiryDate
        }