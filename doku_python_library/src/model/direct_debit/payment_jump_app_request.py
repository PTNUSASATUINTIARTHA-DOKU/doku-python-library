from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.direct_debit.url_param import UrlParam
from doku_python_library.src.model.direct_debit.payment_jump_app_additional_info import PaymentJumpAppAdditionalInfo
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum

class PaymentJumpAppRequest:

    def __init__(self, partner_reference_no: str, url_param: UrlParam, amount: TotalAmount, additional_info: PaymentJumpAppAdditionalInfo = None,
                 valid_up_to: str = None, point_of_initiation: str = None, ) -> None:
        self.partner_reference_no = partner_reference_no
        self.valid_up_to = valid_up_to
        self.point_of_initiation = point_of_initiation
        self.url_param = url_param
        self.amount = amount
        self.additional_info = additional_info
    

    def create_request_body(self) -> dict:
        return {
            "partnerReferenceNo": self.partner_reference_no,
            "urlParam": self.url_param.json(),
            "amount": self.amount.json(),
            "additionalInfo": self.additional_info.json(),
            "validUpTo": self.valid_up_to,
            "pointOfInitiation": self.point_of_initiation
        }

    def validate_request(self):
        self._validate_direct_debit_channel()
        if self.point_of_initiation is not None:
            self._validate_point_of_initiation()
        self._validate_url_param()

    def _validate_direct_debit_channel(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
    
    def _validate_point_of_initiation(self):
        if self.point_of_initiation.lower() not in ["app", "pc", "mweb"]:
            raise Exception("pointOfInitiation value can only be app/pc/mweb")

    def _validate_url_param(self):
        if self.url_param.type.lower() != "pay_return":
            raise Exception("urlParam.type must always be PAY_RETURN")
        if self.url_param.is_deep_link.lower() not in ["y", "n"]:
            raise Exception("urlParam.isDeepLink can only Y or N")