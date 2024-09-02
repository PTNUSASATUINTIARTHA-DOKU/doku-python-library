from doku_python_library.src.model.direct_debit.account_binding_request import AccountBindingRequest
from doku_python_library.src.model.direct_debit.account_binding_response import AccountBindingResponse
from doku_python_library.src.services.token_service import TokenService
from doku_python_library.src.commons.config import Config
from doku_python_library.src.commons.snap_utils import SnapUtils
from doku_python_library.src.model.general.request_header import RequestHeader
from doku_python_library.src.services.direct_debit_service import DirectDebitService


class DirectDebitController:

    @staticmethod
    def do_account_binding(request: AccountBindingRequest, secret_key: str,
                           client_id: str, device_id: str, ip_address: str, token_b2b: str,
                           is_production: bool) -> AccountBindingResponse:
        timestamp: str = TokenService.get_timestamp()
        endpoint: str = Config.DIRECT_DEBIT_ACCOUNT_BINDING_URL
        method: str = "POST"
        signature: str = TokenService.generate_symmetric_signature(
            http_method=method,
            endpoint=endpoint,
            token_b2b=token_b2b,
            request=request.json(),
            timestamp=timestamp,
            secret_key=secret_key
        )
        external_id: str = SnapUtils.generate_external_id()
        request_header: RequestHeader = SnapUtils.generate_request_header(
            channel_id="SDK",
            client_id=client_id,
            token_b2b=token_b2b,
            timestamp=timestamp,
            external_id=external_id,
            signature=signature,
            device_id=device_id,
            ip_address=ip_address
        )

        return DirectDebitService.do_account_binding_process(request_header=request_header, request=request, is_production=is_production)