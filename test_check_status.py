from doku_python_library.src.commons.config import Config
import unittest
from unittest.mock import patch, Mock, MagicMock
from util import Util
import requests

class TestCheckStatus(unittest.TestCase):

    def setUp(self) -> None:
        self.check_status_url = "/orders/v1.0/transfer-va/status"
    
    def test_check_status_partner_service_id_null(self):
        request = Util.generate_check_status_request()
        request.partner_service_id = None
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
    
    def test_check_status_partner_service_id_not_valid_length(self):
        request = Util.generate_check_status_request()
        request.partner_service_id = "1234"
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId must be exactly 8 characters long and equiped with left-padded spaces. Example: ' 888994'.")

    def test_check_status_partner_service_id_not_valid_format(self):
        request = Util.generate_check_status_request()
        request.partner_service_id = "    890E"
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "partnerServiceId must consist of up to 8 digits of character. Remaining space in case of partner serivce id is less than 8 must be filled with spaces. Example: ' 888994' (2 spaces and 6 digits).")
    
    def test_check_status_customer_no_null(self):
        request = Util.generate_check_status_request()
        request.customer_no = None
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must be a string. Ensure that customerNo is enclosed in quotes. Example: '00000000000000000001'.")

    def test_check_status_customer_no_not_valid_length(self):
        request = Util.generate_check_status_request()
        request.customer_no = "1234567890123456789011"
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must be 20 characters or fewer. Ensure that customerNo is no longer than 20 characters. Example: '00000000000000000001'.")
    
    def test_check_status_customer_no_not_valid_format(self):
        request = Util.generate_check_status_request()
        request.customer_no = "1234567890123456789E"
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "customerNo must consist of only digits. Ensure that customerNo contains only numbers. Example: '00000000000000000001'.")

    def test_check_status_virtual_acc_no_null(self):
        request = Util.generate_check_status_request()
        request.virtual_acc_no = None
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "virtualAccountNo cannot be null. Please provide a virtualAccountNo. Example: ' 88899400000000000000000001'.")

    def test_check_status_virtual_acc_no_not_valid_format(self):
        request = Util.generate_check_status_request()
        request.virtual_acc_no = "TEST123"
        self.assertTrue(request.virtual_acc_no != request.partner_service_id+request.customer_no, "virtualAccountNo is not partnerServiceId + customerNo")

    def test_check_status_payment_request_id_max(self):
        request = Util.generate_check_status_request()
        request.payment_request_id = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "paymentRequestId must be 128 characters or fewer. Ensure that paymentRequestId is no longer than 128 characters. Example: ‘abcdef-123456-abcdef’.")

    def test_check_status_inquiry_request_id_max(self):
        request = Util.generate_check_status_request()
        request.inquiry_request_id = "ImCyDjTlTqJu9Rrq1uSuKxNNqcNdcD8EuXigmUMZsge3fvkSOyZ8FwMfyDGeOXxaDENzXzHrnXTfHIqXaKLz5Uq7zaGkjNL0DiTRn7vnBEigFFkJlhftfqiT2ml82pYI1ZUmuuR3N1zaAQNYZvg3asANmoDVGmJYnMdGTyWtD3PPb2t8Nwm57Qd1BfSZIiC7A4cGFSyzYZNp2ObxP4zUeMoa0TPV2WbnLKJ761qP594vMXt9Om4pzdcwK3aAWHQd"
        with self.assertRaises(Exception) as context:
            request.validate_check_status_request()
        self.assertEqual(str(context.exception.args[0]), "inquiryRequestId must be 128 characters or fewer. Ensure that inquiryRequestId is no longer than 128 characters. Example: ‘abcdef-123456-abcdef’.")

if __name__ == "__main__":
    unittest.main()