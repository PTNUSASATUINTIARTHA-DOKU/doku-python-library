from doku_python_library.src.model.va.check_status_va_data import CheckStatusVAData
from doku_python_library.src.model.va.check_status_additional_info_response import CheckStatusAdditionalInfoResponse

class CheckStatusVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: CheckStatusVAData = None, 
                 additionalInfo: CheckStatusAdditionalInfoResponse = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData
        self.additional_info = additionalInfo
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message
        }
        if self.virtual_account_data is not None:
            response["virtualAccountData"] = self.virtual_account_data
        if self.additional_info is not None:
            response["additionalInfo"] = self.additional_info
        return response