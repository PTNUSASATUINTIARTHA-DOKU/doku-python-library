from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock
from util import Util
import requests

class TestCheckStatus(unittest.TestCase):

    def setUp(self) -> None:
        self.check_status_url = "/orders/v1.0/debit/status"
    
    @patch('requests.post')
    def test_check_status_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_check_status_response("2005500")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_check_status_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.check_status_url, json=request.create_request_body())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.check_status_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)