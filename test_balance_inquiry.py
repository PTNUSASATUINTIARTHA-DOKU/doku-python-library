from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock
from util import Util
import requests

class TestBalanceInquiry(unittest.TestCase):

    def setUp(self) -> None:
        self.balance_inquiry_url = "/direct-debit/core/v1/balance-inquiry"
    
    @patch('requests.post')
    def test_balance_inquiry_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_balance_inquiry_response("2001100")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_balance_inquiry_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.balance_inquiry_url, json=request.create_request_body())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.balance_inquiry_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    def test_balance_inquiry_channel_invalid(self):
        request = Util.generate_balance_inquiry_request()
        request.additional_info.channel = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")