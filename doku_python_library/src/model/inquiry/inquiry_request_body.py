from doku_python_library.src.model.inquiry.inquiry_request_additional_info import InquiryRequestAdditionalInfo
from doku_python_library.src.model.inquiry.inquiry_response_body import InquiryResponseBody

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

    def create_request_body(self) -> dict:
        request: dict = {
            "partnerServiceId": self.partner_service_id,
            "customerNo": self.customer_no,
            "virtualAccountNo": self.virtual_acc_no,
            "channelCode": self.channel_code,
            "trxDateInit": self.trx_date_init,
            "language": self.language,
            "inquiryRequestId": self.inquiry_request_id,
            "additionalInfo": self.additional_info
            
        }    
        return request
    def check_simulator(self, is_production: bool) -> InquiryResponseBody:
        if is_production == False:
            if self.virtual_acc_no.lstrip().startswith("1117"):
                return InquiryResponseBody(responseCode="2002400", responseMessage="success")
            elif self.virtual_acc_no.lstrip().startswith("119"):
                return InquiryResponseBody(responseCode="4042412", responseMessage="Bill not found")

