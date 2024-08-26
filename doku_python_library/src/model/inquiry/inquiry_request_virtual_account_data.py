from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.inquiry.inquiry_reason import InquiryReason
from doku_python_library.src.model.inquiry.inquiry_request_additional_info import InquiryRequestAdditionalInfo

class InquiryRequestVirtualAccountData:

    def __init__(self, partnerServiceId: str, customerNo: str, virtualAccountNo: str,
                 virtualAccountName: str, virtualAccountEmail: str,
                 totalAmount: TotalAmount, virtualAccountTrxType: str, expiredDate: str,
                 additionalInfo: InquiryRequestAdditionalInfo, inquiryStatus: str, inquiryReason: InquiryReason, inquiryRequestId: str, 
                 trxId: str = None, virtualAccountPhone: str = None) -> None:
        self.partner_service_id = partnerServiceId
        self.customer_no = customerNo
        self.virtual_acc_no = virtualAccountNo
        self.virtual_acc_name = virtualAccountName
        self.virtual_acc_email = virtualAccountEmail
        self.virtual_acc_phone = virtualAccountPhone
        self.total_amount = totalAmount
        self.virtual_acc_trx_type = virtualAccountTrxType
        self.expired_date = expiredDate
        self.additional_info = additionalInfo
        self.inquiry_status = inquiryStatus
        self.inquiry_reason = inquiryReason
        self.inquiry_request_id = inquiryRequestId
        self.trx_id = trxId

    def json(self) -> dict:
        return {
            "partnerServiceId": self.partner_service_id,
            "customerNo": self.customer_no,
            "virtualAccountNo": self.virtual_acc_no,
            "virtualAccountName": self.virtual_acc_name,
            "virtualAccountEmail": self.virtual_acc_email,
            "virtualAccountPhone": None if self.virtual_acc_phone is None else self.virtual_acc_phone,
            "totalAmount": self.total_amount.json(),
            "virtualAccountTrxType": self.virtual_acc_trx_type,
            "expiredDate": self.expired_date,
            "additionalInfo": self.additional_info.json(),
            "inquiryStatus": self.inquiry_status,
            "inquiryReason": self.inquiry_reason.json(),
            "inquiryRequestId": self.inquiry_request_id,
            "trxId": None if self.trx_id is None else self.trx_id
        }