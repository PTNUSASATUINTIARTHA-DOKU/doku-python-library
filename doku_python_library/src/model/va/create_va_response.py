from doku_python_library.src.model.va.virtual_account_data import VirtualAccountData

class CreateVAResponse:

    def __init__(self, 
                 responseCode: str, 
                 responseMessage: str, 
                 virtualAccountData: VirtualAccountData = None
                 ) -> None:
        self.response_code = responseCode
        self.response_message =responseMessage
        self.virtual_account_data = virtualAccountData


    def json(self) -> dict:
        response: dict = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message,
        }
        if self.virtual_account_data is not None:
            response["virtualAccountData"] = self.virtual_account_data
        return response