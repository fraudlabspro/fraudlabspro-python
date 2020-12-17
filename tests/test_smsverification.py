# -*- coding: utf-8 -*-

import pytest
import json

from fraudlabspro.smsverification import SMSVerification

def testsendsms(global_data):
    sms_verification_variables = {
        'key': global_data["apikey"],
        'tel': '+123456789',
        'country_code': 'US',
        'mesg': 'Hi, your OTP is <otp>.',
        'otp_timeout': 3600,
    }
    result = json.loads(SMSVerification.send_sms(sms_verification_variables))
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert result['error'] == "API key not found."
    else:
        assert result['error'] == "Invalid phone number."


def testverifysms(global_data):
    verify_sms_variables = {
        'key': global_data["apikey"],
        'tran_id': 'UNIQUE_TRANS_ID',
        'otp': 'OTP_RECEIVED',
    }
    result = json.loads(SMSVerification.verify_sms(verify_sms_variables))
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert result['error'] == "API key not found."
    else:
        assert result['error'] == "Invalid OTP."

def testfunctionexist():
    errors = []
    functions_list = ['send_sms', 'verify_sms']
    for x in range(len(functions_list)): 
        # assert hasattr(SMSVerification, functions_list[x]) == True, "Function did not exist."
        if (hasattr(SMSVerification, functions_list[x]) == False):
            errors.append("Function " + functions_list[x] + " did not exist.")
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))
