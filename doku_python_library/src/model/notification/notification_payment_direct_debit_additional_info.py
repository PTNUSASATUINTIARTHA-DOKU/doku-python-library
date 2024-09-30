from doku_python_library.src.model.direct_debit.line_items import LineItems

class NotificationPaymentDirectDebitAdditionalInfo:

    def __init__(self, channel_id: str = None, acquirer_id: str = None, cust_id_merchant: str = None,
                 account_type: str = None, line_items: list[LineItems] = None) -> None:
        self.channel_id = channel_id
        self.acquirer_id = acquirer_id
        self.cust_id_merchant = cust_id_merchant
        self.account_type = account_type
        self.line_items = line_items
    
    def json(self) -> dict:
        request_json = {}
        request_json["channelId"] = self.channel_id if self.channel_id is not None else None
        request_json["acquirerId"] = self.acquirer_id if self.acquirer_id is not None else None
        request_json["custIdMerchant"] = self.cust_id_merchant if self.cust_id_merchant is not None else None
        request_json["accountType"] = self.account_type if self.account_type is not None else None
        if self.line_items is not None:
            items = []
            for item in self.line_items:
                items.append(item.json())
            request_json["lineItems"] = items
        return request_json