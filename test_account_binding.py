from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock, MagicMock
from util import Util
import requests

class TestAccountBinding(unittest.TestCase):

    def setUp(self) -> None:
        self.account_binding_url = "/direct-debit/core/v1/registration-account-binding"
    
    @patch('requests.post')
    def test_account_binding_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_account_binding_response("2000700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_account_binding_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.account_binding_url, json=request.json())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.account_binding_url, json=request.json())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    def test_account_binding_phone_null(self, mock_data):
        request = Util.generate_account_binding_request()
        request.phone_no = None
        with self.assertRaises(Exception) as context:
            request.validate_va_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
    