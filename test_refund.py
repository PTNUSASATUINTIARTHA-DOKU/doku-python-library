from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock
from util import Util
import requests

class TestRefund(unittest.TestCase):

    def setUp(self) -> None:
        self.refund_url = "/direct-debit/core/v1/debit/refund"
    
    @patch('requests.post')
    def test_refund_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_refund_response("2000700")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_refund_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.refund_url, json=request.create_request_body())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.refund_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    def test_refund_channel_invalid(self):
        request = Util.generate_refund_request()
        request.additional_info.channel = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.channel is not valid. Ensure that additionalInfo.channel is one of the valid channels. Example: 'DIRECT_DEBIT_ALLO_SNAP'.")

    def test_refund_original_partner_ref_max(self):
        request = Util.generate_refund_request()
        request.original_partner_reference_no = "1234123123412312312"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "originalPartnerReferenceNo must be 12 characters or fewer. Ensure that originalPartnerReferenceNo is no longer than 12 characters. Example: 'INV-001'.")