from src.snap import DokuSNAP
from src.model.va.create_va_request import CreateVARequest
from src.model.va.total_amount import TotalAmount
from src.model.va.additional_info import AdditionalInfo

payment: DokuSNAP = DokuSNAP(
    private_key= "/Users/dokuit/DOKU/doku-python-sdk/private_key.pem", 
    client_id="BRN-0201-1690264516387", 
    is_production=False
    )

request: CreateVARequest = CreateVARequest(
    partner_service_id= "  888994",
    virtual_acc_name= "Toru Yamashita",
    trx_id= "23219829713",
    virtual_acc_trx_type= "1",
    total_amount= TotalAmount(value="15000.00", currency="IDR"),
    partner_id= "PARTNER-ID",
    external_id= "EXTERNAL-ID",
    channel_id= "CHANNEL-ID",
    additional_info= AdditionalInfo(channel="VIRTUAL_ACCOUNT_BANK_MANDIRI", reusable="2")
)

payment.createVA(create_va_request= request)
