from doku_python_library.src.model.va.create_va_request import CreateVARequest

class UpdateVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: CreateVARequest=None):
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message
        }
        if self.virtual_account_data is not None:
            response["virtualAccountData"] = self.virtual_account_data
        return response