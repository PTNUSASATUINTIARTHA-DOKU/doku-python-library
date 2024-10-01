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
                 transAmount: TotalAmount = None, feeAmount: TotalAmount = None, paidTime: str = None, refundHistory: list[RefundHistory] = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.service_code = serviceCode
        self.latest_transaction_status = latestTransactionStatus
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
        self.refund_history = refundHistory
    
    def json(self) -> dict:
        response = {}
        response["responseCode"] = self.response_code
        response["responseMessage"] = self.response_message
        response["originalPartnerReferenceNo"] = self.original_partner_reference_no
        response["originalReferenceNo"] = self.original_reference_no
        response["approvalCode"] = self.approval_code
        response["originalExternalId"] = self.original_external_id
        response["serviceCode"] = self.service_code
        response["latestTransactionStatus"] = self.latest_transaction_status
        response["transactionStatusDesc"] = self.transaction_status_desc
        response["originalResponseCode"] = self.original_response_code
        response["originalResponseMessage"] = self.original_response_message
        response["sessionId"] = self.session_id
        response["requestID"] = self.request_id
        response["transAmount"] = self.trans_amount.json() if self.trans_amount != None else None
        response["feeAmount"] = self.fee_amount.json() if self.fee_amount != None else None
        response["paidTime"] = self.paid_time
        response["additionalInfo"] = self.additional_info.json() if self.additional_info != None else None
        history = []
        if self.refund_history is not None:
            for info in self.refund_history:
                history.append(info.json())
        response["refundHistory"] = history
        return response