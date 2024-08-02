import re

class CheckStatusRequest:

    def __init__(self, partner_service_id: str, customer_no: str, virtual_acc_no: str,
                 virtual_acc_name: str = None, inquiry_request_id: str = None, payment_request_id: str = None,
                 additional_info: any = None):
        self.partner_service_id = partner_service_id
        self.customer_no = customer_no
        self.virtual_acc_no = virtual_acc_no
        self.virtual_acc_name = virtual_acc_name
        self.inquiry_request_id =  inquiry_request_id
        self.payment_request_id = payment_request_id
        self.additional_info = additional_info

    def validate_check_status_request(self) -> None:
        self._validate_partner_service_id()
        self._validate_customer_no()
        if self.inquiry_request_id is not None:
            self._validate_inquiry_request_id()
        if self.payment_request_id is not None:
            self._validate_payment_request_id()
    
    def _validate_partner_service_id(self) -> None:
        pattern = r'^\s{0,7}\d{1,8}$' 
        value: str = self.partner_service_id
        if value is None:
            raise Exception("partnerServiceId cannot be null. Please provide a partnerServiceId. Example: ' 888994'.")
        elif len(value) != 8:
            raise Exception("partnerServiceId must be exactly 8 characters long and equiped with left-padded spaces. Example: ' 888994'.")
        elif not isinstance(value, str):
            raise Exception("partnerServiceId must be a string. Ensure that partnerServiceId is enclosed in quotes. Example: ' 888994'.")
        elif not re.match(pattern, value):
            raise Exception("partnerServiceId must consist of up to 8 digits of character. Remaining space in case of partner serivce id is less than 8 must be filled with spaces. Example: ' 888994' (2 spaces and 6 digits).")
        
    def _validate_customer_no(self) -> None:
        pattern = r'^\d+$'
        value: str = self.customer_no
        if value is None:
            raise Exception("customerNo must be a string. Ensure that customerNo is enclosed in quotes. Example: '00000000000000000001'.")
        elif len(value) > 20:
            raise Exception("customerNo must be 20 characters or fewer. Ensure that customerNo is no longer than 20 characters. Example: '00000000000000000001'.")
        elif not re.match(pattern, value):
            raise Exception("customerNo must consist of only digits. Ensure that customerNo contains only numbers. Example: '00000000000000000001'.")
        self._validate_virtual_acc_no()
    
    def _validate_virtual_acc_no(self) -> None:
        va_no: str = self.virtual_acc_no
        value: str = self.customer_no
        if va_no is None:
            raise Exception("virtualAccountNo cannot be null. Please provide a virtualAccountNo. Example: ' 88899400000000000000000001'.")
        elif not va_no.isascii():
            raise Exception("virtualAccountNo must be a string. Ensure that virtualAccountNo is enclosed in quotes. Example: ' 88899400000000000000000001'.")
        elif va_no != (self.partner_service_id + value):
            raise Exception("virtualAccountNo must be the concatenation of partnerServiceId and customerNo. Example: ' 88899400000000000000000001' (where partnerServiceId is ' 888994' and customerNo is '00000000000000000001').")
        
    def _validate_inquiry_request_id(self) -> None:
        value: str = self.inquiry_request_id
        if not isinstance(value, str):
            raise Exception("inquiryRequestId must be a string. Ensure that inquiryRequestId is enclosed in quotes. Example: ‘abcdef-123456-abcdef’")
        elif len(value) > 128:
            raise Exception("inquiryRequestId must be 128 characters or fewer. Ensure that inquiryRequestId is no longer than 128 characters. Example: ‘abcdef-123456-abcdef’.")
    
    def _validate_payment_request_id(self) -> None:
        value: str = self.payment_request_id
        if not isinstance(value, str):
            raise Exception("paymentRequestId must be a string. Ensure that paymentRequestId is enclosed in quotes. Example: ‘abcdef-123456-abcdef’.")
        elif len(value) > 128:
            raise Exception("paymentRequestId must be 128 characters or fewer. Ensure that paymentRequestId is no longer than 128 characters. Example: ‘abcdef-123456-abcdef’.")
        
    
    def create_request_body(self) -> dict:
        request: dict = {
            "partnerServiceId": self.partner_service_id,
            "customerNo": self.customer_no,
            "virtualAccountNo": self.virtual_acc_no
        }
        if self.virtual_acc_name is not None:
            request["virtualAccountName"] = self.virtual_acc_name
        if self.inquiry_request_id is not None:
            request["inquiryRequestId"] = self.inquiry_request_id
        if self.payment_request_id is not None:
            request["paymentRequestId"] = self.payment_request_id
        if self.additional_info is not None:
            request["additionalInfo"] = self.additional_info
        return request