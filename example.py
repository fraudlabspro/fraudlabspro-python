# import SDK to use the function
from libs.order import Order
from libs.smsverification import SMSVerification

 # Configure your API key
api_key = 'YOUR_API_KEY'


"""
# Here is an example to validate order details.
# Set your variables here and then pass the values through the Python library.
"""
order_details_variables = {
	'key': api_key,
	'ip': '146.112.62.105',
	'order': {
		'order_id': '67398', 
		'currency': 'USD',
		'amount': '42',
		'quantity': 1, 
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
		'country': 'US',
	},
	'shipping': {
		'address': '4469 Chestnut Street',
		'city'   : 'Tampa',
		'state'  : 'FL',
		'postcode': '33602',
		'country': 'US',
	}
}
print(Order.validate(order_details_variables))


"""
# Here is an example to get transaction details.
# API key is your api key.
# id is either FraudLabs Pro transaction ID or Order ID.
# type is id type, which define either the id is FraudLabsPrp::FLP_ID or FraudLabsPro::ORDER_ID.
"""
get_transaction_variables = {
	'key': api_key,
	'id': '20180705-WISXW2',
	'id_type': 'FraudLabsPro::FLP_ID'
}
print(Order.get_transaction(get_transaction_variables))

"""
 # Here is example of send feecback of either approve or reject this particular order.
"""
feedback_variables = {
	'key': api_key,
	'id': '20180705-WISXW2',
	# Three actions available: APPROVE, REJECT, REJECT_BLACKLIST
	'action': 'APPROVE',
	'notes': 'This is for testing purpose.',
}
print(Order.feedback(feedback_variables))

"""
 # Here is example of verify the valid order by send the SMS to customer.
"""
sms_verification_variables = {
	'key': api_key,
	'tel': '+60175063088',
	'country_code': 'MY',
	'mesg': 'Your OTP for the transaction is <otp>.',
}
print(SMSVerification.send_sms(sms_verification_variables))

"""
 # Here is example of check the SMS verification result of the particular order.
"""
verify_sms_variables = {
	'key': api_key,
	'tran_id': 'LcV6tHszNaiEAB6U7ZRy',
	'otp': '971504',
}
print(SMSVerification.verify_sms(verify_sms_variables))


