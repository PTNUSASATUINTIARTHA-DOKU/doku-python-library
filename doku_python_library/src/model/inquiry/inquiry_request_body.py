from doku_python_library.src.model.inquiry.inquiry_request_additional_info import InquiryRequestAdditionalInfo

class InquiryRequestBody:

    def __init__(self, partner_service_id: str, customer_no: str, virtual_acc_no: str,
                 channel_code: str, trx_date_init: str, language: str, inquiry_request_id: str,
                 additional_info: InquiryRequestAdditionalInfo) -> None:
        self.partner_service_id = partner_service_id
        self.customer_no = customer_no
        self.virtual_acc_no = virtual_acc_no
        self.channel_code = channel_code
        self.trx_date_init = trx_date_init
        self.language = language
        self.inquiry_request_id = inquiry_request_id
        self.additional_info = additional_info