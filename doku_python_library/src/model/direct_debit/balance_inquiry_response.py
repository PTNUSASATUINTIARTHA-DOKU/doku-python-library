from doku_python_library.src.model.direct_debit.account_info import AccountInfo

class BalanceInquiryResponse:

    def __init__(self, responseCode: str, responseMessage: str, accountInfos: list[AccountInfo] = None) -> None:
        self.response_code = responseCode
        self.response_message = responseMessage
        self.account_infos = accountInfos
    
    def json(self) -> dict:
        response = {
            "responseCode": self.response_code,
            "responseMessage": self.response_message
        }
        infos = []
        if self.account_infos is not None:
            for info in self.account_infos:
                infos.append(info.json())
        response["accountInfos"] = infos
        return response