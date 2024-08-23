from doku_python_library.src.model.inquiry.inquiry_request_virtual_account_data import InquiryRequestVirtualAccountData
class InquiryResponseBody:
    
    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: InquiryRequestVirtualAccountData = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData
    
    def json(self) -> dict:
        return {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
            "virtualAccountData": self.virtual_account_data.json()
        }