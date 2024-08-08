from doku_python_library.src.model.va.check_status_va_data import CheckStatusVAData

class CheckStatusVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: CheckStatusVAData = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_account_data = virtualAccountData