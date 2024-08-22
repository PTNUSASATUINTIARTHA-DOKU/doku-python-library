from doku_python_library.src.model.va.additional_info import AdditionalInfo


class NotificationVirtualAccountData:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str, 
                 virtualAccountName: str, paymentRequestId: str, additionalInfo: AdditionalInfo) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.payment_request_id = paymentRequestId
        self.additional_info = additionalInfo