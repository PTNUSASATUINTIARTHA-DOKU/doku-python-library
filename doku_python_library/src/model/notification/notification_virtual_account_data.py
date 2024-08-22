from doku_python_library.src.model.va.additional_info import AdditionalInfo


class NotificationVirtualAccountData:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str, 
                 virtualAccountName: str, paymentRequestId: str, additionalInfo: AdditionalInfo = None) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.payment_request_id = paymentRequestId
        self.additional_info = additionalInfo

    def json(self) -> dict:
        return {
            "partnerServiceId": self.partner_service_id,
            "customerNo": self.customer_no,
            "virtualAccountNo": self.virtual_acc_no,
            "virtualAccountName": self.virtual_acc_name,
            "paymentRequestId": self.payment_request_id,
            "additionalInfo": None if self.additional_info is None else self.additional_info.json()
        }