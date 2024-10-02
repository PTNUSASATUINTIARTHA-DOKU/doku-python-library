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
    
    def test_refund_refund_amount_value_invalid(self):
        request = Util.generate_refund_request()
        request.refund_amount.value = "1234123123412312312"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.value is an invalid format")
    
    def test_refund_refund_amount_currency_invalid(self):
        request = Util.generate_refund_request()
        request.refund_amount.currency = "JPY"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.currency must be 'IDR'. Ensure that totalAmount.currency is 'IDR'. Example: 'IDR'.")
    
    def test_refund_partner_refund_no_null(self):
        request = Util.generate_refund_request()
        request.partner_refund_no = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "partnerRefundNo cannot be null. Please provide a partnerRefundNo. Example: 'INV-0001'.")

    def test_refund_partner_refund_no_max(self):
        request = Util.generate_refund_request()
        request.partner_refund_no = "1234567890123"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "partnerRefundNo must be 12 characters or fewer. Ensure that partnerRefundNo is no longer than 12 characters. Example: 'INV-REF-001'.")