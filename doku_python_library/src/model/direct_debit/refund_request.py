from doku_python_library.src.model.direct_debit.refund_additional_info import RefundAdditionalInfo
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class RefundRequest:

    def __init__(self, original_partner_reference_no: str, refund_amount: TotalAmount, partner_refund_no: str,
                 additional_info: RefundAdditionalInfo, original_external_id: str = None, reason: str = None) -> None:
        self.original_partner_reference_no = original_partner_reference_no
        self.refund_amount = refund_amount
        self.partner_refund_no = partner_refund_no
        self.additional_info = additional_info
        self.original_external_id = original_external_id
        self.reason = reason

    def create_request_body(self) -> dict:
        return {
            "originalPartnerReferenceNo": self.original_partner_reference_no,
            "refundAmount": self.refund_amount.json(),
            "partnerRefundNo": self.partner_refund_no,
            "additionalInfo": self.additional_info.json(),
            "originalExternalId": self.original_external_id,
            "reason": self.reason
        }

    def validate_request(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")