from doku_python_library.src.model.va.update_va import UpdateVADto

class UpdateVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: UpdateVADto):
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData