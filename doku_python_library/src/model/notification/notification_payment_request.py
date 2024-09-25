from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.va.additional_info import AdditionalInfo

class PaymentNotificationAdditionalInfo:

    def __init__(self, channel: str, sender_name: str, source_account_no: str, source_bank_code: str,
                 source_bank_name: str) -> None:
        self.sender_name = sender_name
        self.source_account_no = source_account_no
        self.source_bank_code = source_bank_code
        self.source_bank_name = source_bank_name

class PaymentNotificationRequest:

    def __init__(self, partnerServiceId: str = None, customerNo: str = None, virtualAccountNo: str = None,
                 virtualAccountName: str = None, trxId: str = None, paymentRequestId: str = None, trxDateTime: str = None,
                 paidAmount: TotalAmount = None, virtualAccountEmail: str = None, virtualAccountPhone: str = None, additionalInfo: AdditionalInfo = None, virtualAccountTrxType: str = None,
                 expiredDate: str = None) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.trx_id = trxId
        self.payment_request_id = paymentRequestId
        self.paid_amount = paidAmount
        self.virtual_acc_email = virtualAccountEmail
        self.virtual_acc_phone = virtualAccountPhone
        self.additional_info = additionalInfo
        self.virtual_acc_trx_type = virtualAccountTrxType
        self.expired_date = expiredDate
        self.trx_date_time = trxDateTime
