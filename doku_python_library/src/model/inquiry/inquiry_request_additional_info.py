
class InquiryRequestAdditionalInfo:

    def __init__(self, channel: str,  minAmount: str = None, maxAmount: str = None, trxId: str = None) -> None:
        self.channel = channel
        self.min_amount = minAmount
        self.max_amount = maxAmount
        self.trx_id = trxId
    
    def json(self) -> dict:
        return {
            "channel": self.channel,
            "minAmount": self.min_amount,
            "maxAmount": self.max_amount,
            "trxId": self.trx_id
        }