from doku_python_library.src.model.direct_debit.account_binding_additional_info_request import AccountBindingAdditionalInfoRequest
from doku_python_library.src.commons.direct_debit_enum import DirectDebitEnum


class AccountBindingRequest:

    def __init__(self, phone_no: str, additional_info: AccountBindingAdditionalInfoRequest) -> None:
        self.phone_no = phone_no
        self.additional_info = additional_info
    
    def json(self) -> dict:
        return {
            "phoneNo": self.phone_no,
            "additionalInfo": self.additional_info.json()
        }
    
    def validate_request(self):
        self._validate_direct_debit_channel()
        self._validate_allo_bank()

    def _validate_direct_debit_channel(self):
        dd_enum = [e.value for e in DirectDebitEnum]
        if self.additional_info.channel not in dd_enum:
            raise Exception("additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")
        
    def _validate_allo_bank(self):
        if self.additional_info.channel == DirectDebitEnum.DIRECT_DEBIT_ALLO_SNAP.value:
            self._validate_required_device_information()
            self._validate_os_type()
            self._validate_channel_id()
    
    def _validate_required_device_information(self):
        if self.additional_info.device_model is None or self.additional_info.os_type is None or self.additional_info.channel_id is None:
                raise Exception("Value device_model, os_type, channel_id cant be null for DIRECT_DEBIT_ALLO_SNAP")
    
    def _validate_os_type(self):
        if self.additional_info.os_type.lower() not in ['ios', 'android']:
            raise Exception("osType value can only be ios/android")
    
    def _validate_channel_id(self):
        if self.additional_info.channel_id.lower() not in ['app', 'web']:
            raise Exception("channelId value can only be app/web")