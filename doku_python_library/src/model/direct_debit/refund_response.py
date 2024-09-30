from doku_python_library.src.model.va.total_amount import TotalAmount

class RefundResponse:

    def __init__(self, responseCode: str, responseMessage: str, refundAmount: TotalAmount = None,
                 originalPartnerReferenceNo: str = None, originalReferenceNo: str = None,
                 refundNo: str = None, partnerRefundNo: str = None, refundTime: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.refund_amount = refundAmount
        self.original_partner_reference_no = originalPartnerReferenceNo
        self.original_reference_no = originalReferenceNo
        self.refund_no = refundNo
        self.partner_refund_no = partnerRefundNo
        self.refund_time = refundTime