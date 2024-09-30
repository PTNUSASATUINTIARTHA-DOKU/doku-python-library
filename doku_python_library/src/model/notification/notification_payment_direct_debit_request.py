from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.notification.notification_payment_direct_debit_additional_info import NotificationPaymentDirectDebitAdditionalInfo

class NotificationPaymentDirectDebitRequest:

    def __init__(self, original_partner_reference_no: str, original_reference_no: str, original_external_id: str,
                 latest_transaction_status: str, transaction_status_desc: str, amount: TotalAmount, additional_info: NotificationPaymentDirectDebitAdditionalInfo) -> None:
        self.original_partner_reference_no = original_partner_reference_no
        self.original_reference_no = original_reference_no
        self.original_external_id = original_external_id
        self.latest_transaction_status = latest_transaction_status
        self.transaction_status_desc = transaction_status_desc
        self.amount = amount
        self.additional_info = additional_info

    def json(self) -> dict:
        return {
            "originalPartnerReferenceNo": self.original_partner_reference_no,
            "originalReferenceNo": self.original_reference_no,
            "originalExternalId": self.original_external_id,
            "latestTransactionStatus": self.latest_transaction_status,
            "transactionStatusDesc": self.transaction_status_desc,
            "amount": self.amount.json() if self.amount is not None else None,
            "additionalInfo": self.additional_info.json() if self.additional_info is not None else None
        }