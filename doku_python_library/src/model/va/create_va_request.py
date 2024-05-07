from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.va.additional_info import AdditionalInfo

class CreateVARequest:

    def __init__(self,
                 partner_service_id: str,
                 virtual_acc_name: str,
                 trx_id: str,
                 virtual_acc_trx_type: str,
                 total_amount: TotalAmount,
                 partner_id: str,
                 external_id: str,
                 channel_id: str,
                 customer_no: str = None,
                 virtual_acc_email: str = None,
                 virtual_acc_phone: str = None,
                 additional_info: AdditionalInfo = None,
                 expired_date: str = None
                 ) -> None:
        self.partner_service_id = partner_service_id
        self.virtual_acc_name = virtual_acc_name
        self.trx_id = trx_id
        self.virtual_acc_trx_type = virtual_acc_trx_type
        self.total_amount = total_amount
        self.virtual_acc_email = virtual_acc_email
        self.virtual_acc_phone = virtual_acc_phone
        self.additional_info = additional_info
        self.expired_date = expired_date
        self.partner_id = partner_id
        self.external_id = external_id
        self.channel_id = channel_id
        self.customer_no = customer_no

    def create_request_body(self) -> dict:
        request: dict = {
            "partnerServiceId": self.partner_service_id,
            "virtualAccountName": self.virtual_acc_name,
            "trxId": self.trx_id,
            "totalAmount": self.total_amount.json(),
            "virtualAccountTrxType": self.virtual_acc_trx_type
        }
        if self.virtual_acc_email is not None:
            request["virtualAccountEmail"] = self.virtual_acc_email
        if self.virtual_acc_phone is not None:
            request["virtualAccountPhone"] = self.virtual_acc_phone
        if self.additional_info is not None:
            request["additionalInfo"] = self.additional_info.json()
        return request