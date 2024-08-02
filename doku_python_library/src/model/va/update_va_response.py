from doku_python_library.src.model.va.update_va_request import UpdateVaRequest

class UpdateVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: UpdateVaRequest=None):
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData