from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.direct_debit.check_status_additional_info_response import CheckStatusAdditionalInfoResponse
from doku_python_library.src.model.direct_debit.refund_history import RefundHistory

class CheckStatusResponse:

    def __init__(self, responseCode: str, responseMessage: str, serviceCode: str = None, latestTransactionStatus: str = None,
                 additionalInfo: CheckStatusAdditionalInfoResponse = None, originalReferenceNo: str = None,
                 originalPartnerReferenceNo: str = None, approvalCode: str = None, originalExternalId: str = None,
                 transactionStatusDesc: str = None, originalResponseCode: str = None, originalResponseMessage: str = None,
                 sessionId: str = None, requestID: str = None, refundNo: str = None, partnerRefundNo: str = None,
                 refundAmount: TotalAmount = None, refundStatus: str = None, refundDate: str = None, reason: str = None,
                 transAmount: TotalAmount = None, feeAmount: str = None, paidTime: str = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.service_code = serviceCode
        self.latestTransactionStatus = latestTransactionStatus
        self.additional_info = additionalInfo
        self.original_reference_no = originalReferenceNo
        self.original_partner_reference_no = originalPartnerReferenceNo
        self.approval_code = approvalCode
        self.original_external_id = originalExternalId
        self.transaction_status_desc = transactionStatusDesc
        self.original_response_code = originalResponseCode
        self.original_response_message = originalResponseMessage
        self.session_id = sessionId
        self.request_id = requestID
        self.refund_no = refundNo
        self.partner_refund_no = partnerRefundNo
        self.refund_amount = refundAmount
        self.refund_status = refundStatus
        self.refund_date = refundDate
        self.reason = reason
        self.trans_amount = transAmount
        self.fee_amount = feeAmount
        self.paid_time = paidTime