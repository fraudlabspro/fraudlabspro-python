# -*- coding: utf-8 -*-

import pytest
import json

from fraudlabspro.fraudvalidation import FraudValidation

# def testapikey(global_data):
    # assert global_data["apikey"] == ""

def testinvalidapikey(global_data):
    fraud_validation = FraudValidation(global_data["apikey"])
    order_details_variables = {
        # 'key': global_data["apikey"],
        'ip': '8.8.8.8',
    }
    result = json.loads(fraud_validation.validate(order_details_variables))
    assert result['error']['error_message'] == 'INVALID API KEY'

def testapikeyexist(global_data, capsys):
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        with capsys.disabled():
            print ("You could enter a FraudLabs Pro API Key in tests/conftest.py for real web service calling test.")
            print ("You could sign up for a free API key at https://www.fraudlabspro.com/pricing if you do not have one.")
        assert global_data["apikey"] == "YOUR_API_KEY"
    else:
        assert global_data["apikey"] != "YOUR_API_KEY"

def testfunctionexist():
    fraud_validation = FraudValidation(global_data["apikey"])
    errors = []
    functions_list = ['validate', 'get_transaction', 'feedback']
    for x in range(len(functions_list)): 
        # assert hasattr(Order, functions_list[x]) == True, "Function did not exist."
        # if (hasattr(Order, functions_list[x]) == False):
        if (hasattr(fraud_validation, functions_list[x]) == False):
            errors.append("Function " + functions_list[x] + " did not exist.")
    # assert no error message has been registered, else print messages
    assert not errors, "errors occured:\n{}".format("\n".join(errors))

def testvalidateorder(global_data):
    fraud_validation = FraudValidation(global_data["apikey"])
    order_details_variables = {
        # 'key': global_data["apikey"],
        'ip': '8.8.8.8',
    }
    result = json.loads(fraud_validation.validate(order_details_variables))
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert result['error']['error_message'] == "INVALID API KEY"
    else:
        assert result['ip_country'] == "US"

def testgettransaction(global_data):
    fraud_validation = FraudValidation(global_data["apikey"])
    get_transaction_variables = {
	    # 'key': global_data["apikey"],
	    'id': '20170906MXFHSTRF',
	    # 'id_type': 'FraudLabsPro::FLP_ID' # No longer supported in v2
    }
    result = json.loads(fraud_validation.get_transaction(get_transaction_variables))
    assert result['error']['error_message'] == 'TRANSACTION NOT FOUND'

def testfeedback(global_data):
    fraud_validation = FraudValidation(global_data["apikey"])
    feedback_variables = {
	    # 'key': global_data["apikey"],
	    'id': '20170906MXFHSTRF',
	    'action': 'APPROVE',
	    'notes': 'This customer made a valid purchase before.',
    }
    result = json.loads(fraud_validation.feedback(feedback_variables))
    if (global_data["apikey"] == 'YOUR_API_KEY'):
        assert result['error']['error_message'] == "INVALID API KEY"
    else:
        assert result['error']['error_message'] == "INVALID TRANSACTION ID"