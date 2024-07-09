from doku_python_library.src.model.va.check_status_payment_flag_response import CheckStatusPaymentFlagResponse
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.va.check_status_additional_info_response import CheckStatusAdditionalInfoResponse

class CheckStatusVAData:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str,
                 paidAmount: TotalAmount, billAmount: TotalAmount, additionalInfo: CheckStatusAdditionalInfoResponse,
                 paymentFlagReason: CheckStatusPaymentFlagResponse = None, inquiryRequestId: str = None, paymentRequestId: str = None,
                 virtualAccountNumber: str = None) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no: virtualAccountNo
        self.paid_amount = paidAmount
        self.bill_amount = billAmount
        self.additional_info = additionalInfo
        self.payment_flag_reason = paymentFlagReason
        self.inquiry_request_id = inquiryRequestId
        self.payment_request_id = paymentRequestId
        self.virtual_acc_number = virtualAccountNumber