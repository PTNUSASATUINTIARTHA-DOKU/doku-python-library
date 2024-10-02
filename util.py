from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest, AccountBindingAdditionalInfoRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
from doku_python_library.src.model.direct_debit.account_unbinding_request import AccountUnbindingAdditionalInfoRequest, AccountUnbindingRequest
from doku_python_library.src.model.direct_debit.account_unbinding_response import AccountUnbindingResponse
from doku_python_library.src.model.direct_debit.card_registration_request import CardRegistrationRequest, CardRegistrationAdditionalInfo
from doku_python_library.src.model.direct_debit.card_registration_response import CardRegistrationResponse
from doku_python_library.src.model.direct_debit.card_unbinding_request import CardUnbindingRequest
from doku_python_library.src.model.direct_debit.card_unbinding_response import CardUnbindingResponse
from doku_python_library.src.model.direct_debit.balance_inquiry_request import BalanceInquiryRequest, BalanceInquiryAdditionalInfo
from doku_python_library.src.model.direct_debit.balance_inquiry_response import BalanceInquiryResponse
from doku_python_library.src.model.direct_debit.check_status_request import CheckStatusRequest
from doku_python_library.src.model.direct_debit.check_status_response import CheckStatusResponse
from doku_python_library.src.model.va.total_amount import TotalAmount
from doku_python_library.src.model.direct_debit.refund_request import RefundRequest, RefundAdditionalInfo
from doku_python_library.src.model.direct_debit.refund_response import RefundResponse

class Util:

    @staticmethod
    def generate_account_binding_request() -> AccountBindingRequest:
        return AccountBindingRequest(
        phone_no="62813941306101",
        additional_info=AccountBindingAdditionalInfoRequest(
            channel="DIRECT_DEBIT_CIMB_SNAP",
            cust_id_merchant="sdjkava4",
            success_registration_url="https://sandbox.doku.com/bo/login/",
            failed_registration_url="https://www.seleniumeasy.com/test",
        )
    )

    @staticmethod
    def generate_account_binding_response(response_code: str) -> AccountBindingResponse:
        return AccountBindingResponse(
            responseCode= response_code,
            responseMessage="Successful"
        )
    
    @staticmethod
    def generate_account_unbinding_request() -> AccountUnbindingRequest:
        return AccountUnbindingRequest(
            token="eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE3MjkwNTA5ODcsImlzcyI6IkRPS1UiLCJjbGllbnRJZCI6IkJSTi0wMjA1LTE3MjcxNzQ2Mzk4MDEiLCJhY2NvdW50SWQiOiIyZjAzYjY1ODdlZDE5ZmJkYjE5MTJjOTEzNzljMTEwZiJ9.S0kMrOOR8_kur2iU3YbzlMkVtWexM_jziYFY1uaJI3bYdNZ7TnPD1ZYOI-_v4tzQn6on0Rozp00_WdQFMmdoXu9lIBkprEz9e2rN2_tg1tUSXPG6SW5umgf9IV0n1Ro2M5Xfvh4zRFboAU4SvqlSbVM57Vk0LBMTWn8ah0NaBIL40p-UB1UfZ8q5-jyshFszS7S59c21fMA8FXFH_Zz6hjk7HWaAjYPPRmuAkEs3liWYaAoGS_eHL0p_t_IpBlOBsMe6dJhpeDllwole7sptJ1Hckux6mSB4zIKUIrQHZW8F3hTCV1Mx1Hkome7e_6f0VJDsclXbe48xWVtidd2C8w",
            additional_info=AccountUnbindingAdditionalInfoRequest(
                channel="DIRECT_DEBIT_CIMB_SNAP"
            )
        )
    
    @staticmethod
    def generate_account_unbinding_response(response_code: str) -> AccountUnbindingResponse:
        return AccountUnbindingResponse(
            responseCode=response_code,
            responseMessage="Successful"
        )
    
    @staticmethod
    def generate_card_registration_request() -> CardRegistrationRequest:
        return CardRegistrationRequest(
            card_data="5cg2G2719+jxU1RfcGmeCyQrLagUaAWJWWhLpm/mbkiTIrb9qA5kQgAZ4jTsMWOgMxB7lJX6k1hiv5Mq4ltG5g==|GbD2PwzJIgpPijLs14BwZQ==",
            cust_id_merchant="sdkpython",
            phone_no="62819919121",
            additionalInfo=CardRegistrationAdditionalInfo(
                channel="DIRECT_DEBIT_BRI_SNAP",
                success_registration_url="https://www.doku.com",
                failed_registration_url="https://www.doku.com"
            )
        )
    
    @staticmethod
    def generate_card_registration_response(response_code: str) -> CardRegistrationResponse:
        return CardRegistrationResponse(
            responseCode=response_code,
            responseMessage="Successful"
        )
    
    @staticmethod
    def generate_card_unbinding_request() -> CardUnbindingRequest:
        return CardUnbindingRequest(
            token="eyJhbGciOiJSUzI1NiJ9.eyJleHAiOjE3MjkwNTA5ODcsImlzcyI6IkRPS1UiLCJjbGllbnRJZCI6IkJSTi0wMjA1LTE3MjcxNzQ2Mzk4MDEiLCJhY2NvdW50SWQiOiIyZjAzYjY1ODdlZDE5ZmJkYjE5MTJjOTEzNzljMTEwZiJ9.S0kMrOOR8_kur2iU3YbzlMkVtWexM_jziYFY1uaJI3bYdNZ7TnPD1ZYOI-_v4tzQn6on0Rozp00_WdQFMmdoXu9lIBkprEz9e2rN2_tg1tUSXPG6SW5umgf9IV0n1Ro2M5Xfvh4zRFboAU4SvqlSbVM57Vk0LBMTWn8ah0NaBIL40p-UB1UfZ8q5-jyshFszS7S59c21fMA8FXFH_Zz6hjk7HWaAjYPPRmuAkEs3liWYaAoGS_eHL0p_t_IpBlOBsMe6dJhpeDllwole7sptJ1Hckux6mSB4zIKUIrQHZW8F3hTCV1Mx1Hkome7e_6f0VJDsclXbe48xWVtidd2C8w",
            additional_info=AccountUnbindingAdditionalInfoRequest(
                channel="DIRECT_DEBIT_BRI_SNAP"
            )
        )

    @staticmethod
    def generate_card_unbinding_response(response_code: str) -> CardUnbindingResponse:
        return CardUnbindingResponse(
            responseCode=response_code,
            responseMessage="Successful"
        )
    
    @staticmethod
    def generate_balance_inquiry_request() -> BalanceInquiryRequest:
        return BalanceInquiryRequest(
            additional_info= BalanceInquiryAdditionalInfo(
                channel="DIRECT_DEBIT_CIMB_SNAP"
            )
        )
    
    @staticmethod
    def generate_balance_inquiry_response(response_code: str) -> BalanceInquiryResponse:
        return BalanceInquiryResponse(
            responseCode=response_code,
            responseMessage="Successful"
        )
    
    @staticmethod
    def generate_check_status_request() -> CheckStatusRequest:
        return CheckStatusRequest(
            service_code="55",
            amount=TotalAmount(
                value="1500.00",
                currency="IDR"
            )
        )
    
    @staticmethod
    def generate_check_status_response(response_code: str) -> CheckStatusResponse:
        return CheckStatusResponse(
            responseCode=response_code,
            responseMessage="Successful"
        )
    
    @staticmethod
    def generate_refund_request() -> RefundRequest:
        return RefundRequest(
            original_partner_reference_no="sdkpython",
            refund_amount= TotalAmount(
                value="1200.00",
                currency="IDR"
            ),
            partner_refund_no="REF1",
            additional_info=RefundAdditionalInfo(
                channel="DIRECT_DEBIT_CIMB_SNAP"
            )
        )
    
    @staticmethod
    def generate_refund_response(response_code: str) -> RefundResponse:
        return RefundResponse(
            responseCode=response_code,
            responseMessage="Successful"
        )