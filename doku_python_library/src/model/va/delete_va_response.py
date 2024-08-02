from doku_python_library.src.model.va.delete_va_virtual_acc_data import DeleteVAResponseVirtualAccountData

class DeleteVAResponse:

    def __init__(self, responseCode: str, responseMessage: str, virtualAccountData: DeleteVAResponseVirtualAccountData = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.virtual_acc_data = virtualAccountData