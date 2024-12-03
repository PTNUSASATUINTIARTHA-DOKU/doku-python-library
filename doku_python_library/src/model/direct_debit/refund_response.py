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
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
        }
        if self.refund_amount is not None:
            response["refundAmount"] = self.refund_amount
        if self.original_partner_reference_no is not None:
            response["originalPartnerReferenceNo"] = self.original_partner_reference_no
        if self.original_reference_no is not None:
            response["originalReferenceNo"] = self.original_reference_no
        if self.refund_no is not None:
            response["refundNo"] = self.refund_no
        if self.partner_refund_no is not None:
            response["partnerRefundNo"] = self.partner_refund_no
        if self.refund_time is not None:
            response["refundTime"] = self.refund_time
        return response