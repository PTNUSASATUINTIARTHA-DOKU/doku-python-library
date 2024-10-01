from doku_python_library.src.model.direct_debit.line_items import LineItems

class PaymentAdditionalInfoRequest:

    def __init__(self, channel: str = None, remarks: str = None, success_payment_url: str = None,
                 failed_payment_url: str = None, line_items: list[LineItems] = None, payment_type: str = None) -> None:
        self.channel = channel
        self.remarks = remarks
        self.success_payment_url = success_payment_url
        self.failed_payment_url = failed_payment_url
        self.line_items = line_items
        self.payment_type = payment_type
    
    def json(self) -> dict:
        items = []
        if self.line_items != None:
            for item in self.line_items:
                items.append(item.json())
        return {
            "channel": self.channel,
            "remarks": self.remarks,
            "successPaymentUrl": self.success_payment_url,
            "failedPaymentUrl": self.failed_payment_url,
            "lineItems": items,
            "paymentType": self.payment_type
        }