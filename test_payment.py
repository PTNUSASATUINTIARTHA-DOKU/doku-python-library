from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock
from util import Util
import requests

class TestPayment(unittest.TestCase):

    def setUp(self) -> None:
        self.payment_url = "/direct-debit/core/v1/debit/payment-host-to-host"
    
    @patch('requests.post')
    def test_refund_success(self, mock_data):
        mock_resp = Mock()
        resp_dict = Util.generate_payment_response("2005400")
        mock_resp.json.return_value = resp_dict
        mock_data.return_value = mock_resp
        request = Util.generate_payment_request()
        response = requests.post(Config.get_base_url(is_production=False)+self.payment_url, json=request.create_request_body())
        mock_data.assert_called_with(Config.get_base_url(is_production=False)+self.payment_url, json=request.create_request_body())
        self.assertEqual(response.json().response_code, resp_dict.response_code)
    
    def test_payment_remarks_invalid(self):
        request = Util.generate_payment_request()
        request.additional_info.remarks = ""
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "additionalInfo.remarks must be 40 characters or fewer. Ensure that additionalInfo.remarks is no longer than 40 characters. Example: 'remarks'.")

    def test_payment_amount_currency_invalid(self):
        request = Util.generate_payment_request()
        request.additional_info.remarks = "REMARKS"
        request.amount.currency = "JPY"
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.currency must be 'IDR'. Ensure that totalAmount.currency is 'IDR'. Example: 'IDR'.")
    
    def test_payment_amount_value_invalid(self):
        request = Util.generate_payment_request()
        request.additional_info.remarks = "REMARKS"
        request.amount.value = None
        with self.assertRaises(Exception) as context:
            request.validate_request()
        self.assertEqual(str(context.exception.args[0]), "totalAmount.value cant be null")
    