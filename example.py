# import SDK to use the function
from fraudlabspro.order import Order
from fraudlabspro.smsverification import SMSVerification
from fraudlabspro.payment import Payment

 # Configure your API key
api_key = 'YOUR_API_KEY'

order = Order(api_key)

"""
# Here is an example to validate order details.
# Set your variables here and then pass the values through the Python library.
"""
order_details_variables = {
	'ip': '146.112.62.105',
	'order': {
		'order_id': '67398', 
		'currency': 'USD',
		'amount': '42',
		'quantity': 1, 
		'paymentGateway': 'creditcard',
		'paymentMethod': 'creditcard'
	},
	'card': {
		'number': '4556553172971283'
	},
	'billing': {
		'firstName': 'Hector',
		'lastName': 'Henderson',
		'email': 'hh5566@gmail.com',
		'phone': '561-628-8674',
		'address': '1766 Powder House Road',
		'city': 'West Palm Beach',
		'state': 'FL',
		'postcode': '33401',
		'country': 'US'
	},
	'shipping': {
		'firstName': 'Hector',
		'lastName': 'Henderson',
		'address': '4469 Chestnut Street',
		'city'   : 'Tampa',
		'state'  : 'FL',
		'postcode': '33602',
		'country': 'US'
	}
}
print(order.validate(order_details_variables))

"""
# Here is an example to get transaction details.
# API key is your api key.
# id is either FraudLabs Pro transaction ID or Order ID.
# type is id type, which define either the id is FraudLabsPrp::FLP_ID or FraudLabsPro::ORDER_ID.
"""
get_transaction_variables = {
	'id': 'THE_FRAUDLABSPRO_ID',
	# 'id_type': 'FraudLabsPro::FLP_ID' # No longer supported in v2
}
print(order.get_transaction(get_transaction_variables))

"""
 # Here is example of send feecback of either approve or reject this particular order.
"""
feedback_variables = {
	'id': 'THE_FRAUDLABSPRO_ID',
	# Three actions available: APPROVE, REJECT, REJECT_BLACKLIST
	'action': 'APPROVE',
	'notes': 'This is for testing purpose.',
}
print(order.feedback(feedback_variables))

sms_validation = SMSVerification(api_key)

"""
 # Here is example of verify the valid order by send the SMS to customer.
"""
sms_verification_variables = {
	'tel': '+123456789',
	'country_code': 'US',
	'mesg': 'Your OTP for the transaction is <otp>.',
	'otp_timeout': 3600,
}
print(sms_validation.send_sms(sms_verification_variables))

"""
 # Here is example of check the SMS verification result of the particular order.
"""
verify_sms_variables = {
	'tran_id': 'UNIQUE_TRANS_ID',
	'otp': 'OTP_RECEIVED',
}
print(sms_validation.verify_sms(verify_sms_variables))

payment_cls = Payment(api_key)

"""
 # Here is example of report the final payment status of an order.
"""
feedback_variables = {
	'email': 'aaa@mailinator.com',
    'status': '-',
    'message': 'This is a test.'
}

result = payment_cls.feedback(feedback_variables)

print(result)
