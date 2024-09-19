from doku_python_library.src.model.va.delete_va_virtual_acc_data import DeleteVAResponseVirtualAccountData

class DeleteVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: DeleteVAResponseVirtualAccountData = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_acc_data = virtualAccountData
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message
        }
        if self.virtual_acc_data is not None:
            response["virtualAccountData"] = self.virtual_acc_data
        return response