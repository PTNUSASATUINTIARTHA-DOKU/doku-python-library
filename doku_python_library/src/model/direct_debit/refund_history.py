from doku_python_library.src.model.va.total_amount import TotalAmount


class RefundHistory:

    def __init__(self, refundNo: str = None, partnerReferenceNo: str = None, refundAmount: TotalAmount = None,
                 refundDate: str = None, reason: str = None) -> None:
        self.refund_no = refundNo
        self.partner_reference_no = partnerReferenceNo
        self.refund_amount = refundAmount
        self.refund_date = refundDate
        self.reason = reason
    
    def json(self) -> dict:
        return {
            "refundNo": self.refund_no,
            "partnerReferenceNo": self.partner_reference_no,
            "refundAmount": self.refund_amount.json(),
            "refundDate": self.refund_date,
            "reason": self.reason
        }