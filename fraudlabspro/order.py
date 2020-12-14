"""
 # FraudLabsPro Python Library
 # Implements fraud checking solution using FraudLabs Pro service.
 # API key is required, and if you do not have an API key, you may sign up free
 # at at https://www.fraudlabspro.com
 #
 # @copyright 2020 FraudLabs Pro
 # https://www.fraudlabspro.com

"""

import urllib.parse
import urllib.request
import json, hashlib, re
from decimal import Decimal
from decimal import ROUND_UP

"""
 # This function is to hashes a string to protect its real value.
"""
class HashText:
    def hash_function(value):
        hash = "fraudlabspro_" + value
        for i in range(65536):
            hash = hashlib.sha1(hash.encode('utf-8')).hexdigest() 
        return hash

"""
 # FraudLabsPro Order module.
 #
 # Validates order for possible fraud and feedback user decision.
"""

class Order:
    """
    # Validate order for possible fraud. Return the result in json format.
    #
    # Result will be return in json format.
    """
    def validate(dictionary):
        # Capture variable and store in local variable
        if 'key' in dictionary:
            api_key = dictionary['key']
        else:
            return ('The API key is required. Please obtain through here: https://www.fraudlabspro.com/pricing')
        #  The IP address.
        if 'ip' in dictionary:
            ipaddr = dictionary['ip']
        else:
            return ('The IP address is required.')
        #  flp_check_sum: Checksum for the device validation. Visit here to learn more: https://www.fraudlabspro.com/developer/javascript
        if 'flp_check_sum' in dictionary:
            flp_check_sum = dictionary['flp_check_sum']
        else:
            flp_check_sum = ''
        #  Order information
        if 'order' in dictionary:  
            if 'order_id' in dictionary['order']:
                user_order_id = dictionary['order']['order_id']
            else:
                user_order_id = ''
            if 'order_note' in dictionary['order']:
                user_order_memo = dictionary['order']['order_note']
            else:
                user_order_memo = ''
            if 'currency' in dictionary['order']:
                currency = dictionary['order']['currency']
                if currency.isalpha() and len(currency) == 3:
                    currency = currency
                else:
                    return 'The currency must contain only 3 letters, complying the ISO-4217.'
            else:
                currency = 'USD'
            if 'amount' in dictionary['order']:
                amount = dictionary['order']['amount']
                if len(amount.rsplit('.')[-1]) == 2:
                    amount = amount
                else:
                    amount = Decimal(amount).quantize(Decimal('.01'), rounding = ROUND_UP)
            else:
                amount = ''
            if 'quantity' in dictionary['order']:
                quantity = dictionary['order']['quantity']
            else:
                quantity = ''
            if 'paymentMethod' in dictionary['order']:
                payment_mode = dictionary['order']['paymentMethod']
            else:
                payment_mode = ''
            if 'department' in dictionary['order']:
                department = dictionary['order']['department']
            else:
                department = ''
        else:
            user_order_id = ''
            user_order_memo = ''
            currency = 'USD'
            amount = ''
            quantity = ''
            payment_mode = ''
            department = ''
        #  Credit card information
        if 'card' in dictionary:
            if 'number' in dictionary['card']:
                card_bin = dictionary['card']['number']
                card_bin = card_bin[:7]
                #  card number need to be hash before send to server.
                card_number = dictionary['card']['number']
                card_hash = HashText.hash_function(card_number)
            else:
                card_bin = ''
                card_number = ''
                card_hash = ''
            if 'avs_result' in dictionary['card']:
                avs_result = dictionary['card']['avs_result']
            else:
                avs_result = ''
            if 'cvv_result' in dictionary['card']:
                cvv_result = dictionary['card']['cvv_result']
            else:
                cvv_result = ''
        else:
            card_bin = ''
            card_number = ''
            card_hash = ''
            avs_result = ''
            cvv_result = ''
        #  Billing information
        if 'billing' in dictionary:
            if 'firstName' in dictionary['billing']:
                first_name = dictionary['billing']['firstName']
            else:
                first_name = ''
            if 'lastName' in dictionary['billing']:
                last_name = dictionary['billing']['lastName']
            else:
                last_name = ''
            if 'username' in dictionary['billing']:
                uname = dictionary['billing']['username']
                #  username need to be hash before send to server.
                username_hash = HashText.hash_function(uname)
            else:
                username_hash = ''
            if 'password' in dictionary['billing']:
                password = dictionary['billing']['password']
                #  password need to be hash before send to server.
                password_hash = HashText.hash_function(password)
            else:
                password_hash = ''
            if 'email' in dictionary['billing']:
                email = dictionary['billing']['email']
                email_domain = email.split('@')[1]
                #  email need to hash before send to server.
                email_hash = HashText.hash_function(email)
            else:
                email = ''
                email_domain = ''
                email_hash = ''
            if 'phone' in dictionary['billing']:
                phone = dictionary['billing']['phone']
                if phone.isdigit():
                    user_phone = phone
                else:
                    user_phone = re.sub('\D','',phone)
            else:
                user_phone = ''
            if 'address' in dictionary['billing']:
                bill_addr = dictionary['billing']['address']
            else:
                bill_addr = ''
            if 'city' in dictionary['billing']:
                bill_city = dictionary['billing']['city']
            else:
                bill_city = ''
            if 'state' in dictionary['billing']:
                bill_state = dictionary['billing']['state']
            else:
                bill_state = ''
            if 'postcode' in dictionary['billing']:
                bill_zip_code = dictionary['billing']['postcode']
            else:
                bill_zip_code = ''
            if 'country' in dictionary['billing']:
                bill_country = dictionary['billing']['country']
            else:
                bill_country = ''
        else:
            first_name = ''
            last_name = ''
            username_hash = ''
            password_hash = ''
            email = ''
            email_domain = ''
            email_hash = ''
            user_phone = ''
            bill_addr = ''
            bill_city = ''
            bill_state = ''
            bill_zip_code = ''
            bill_country = ''
        #  Shipping information
        if 'shipping' in dictionary:
            if 'address' in dictionary['shipping']:
                ship_addr = dictionary['shipping']['address']
            else:
                ship_addr = ''
            if 'city' in dictionary['shipping']:
                ship_city = dictionary['shipping']['city']
            else:
                ship_city = ''
            if 'state' in dictionary['shipping']:
                ship_state = dictionary['shipping']['state']
            else:
                ship_state = ''
            if 'postcode' in dictionary['shipping']:
                ship_zip_code= dictionary['shipping']['postcode']
            else:
                ship_zip_code = ''
            if 'country' in dictionary['shipping']:
                ship_country = dictionary['shipping']['country']
            else:
                ship_country = ''
        else:
            ship_addr = ''
            ship_city = ''
            ship_state = ''
            ship_zip_code = ''
            ship_country = ''
        #  Put all the variables into the array before send to the API
        validate_variable_list = {
                    'key': api_key,
                    'ip': ipaddr,
                    'format': 'json',
                    'source': 'FraudLabsPro Python SDK',
                    'source_version': '3.6.0',
                    'flp_check_sum': flp_check_sum,
                    #  order information
                    'user_order_id': user_order_id,
                    'user_order_memo': user_order_memo,
                    'currency': currency,
                    'amount': amount,
                    'quantity': quantity,
                    'payment_mode': payment_mode,
                    #  credit card information
                    'bin_no': card_bin,
                    'card_hash': card_hash,
                    'avs_result': avs_result,
                    'cvv_result': cvv_result,
                    #  billing information
                    'first_name': first_name,
                    'last_name': last_name,
                    'username_hash': username_hash,
                    'password_hash': password_hash,
                    'email': email,
                    'email_hash': email_hash,
                    'email_domain': email_domain,
                    'user_phone': user_phone,
                    'bill_addr': bill_addr,
                    'bill_city': bill_city,
                    'bill_state': bill_state,
                    'bill_zip_code': bill_zip_code,
                    'bill_country': bill_country,
                    #  shipping information
                    'ship_addr': ship_addr,
                    'ship_city': ship_city,
                    'ship_state': ship_state,
                    'ship_zip_code': ship_zip_code,
                    'ship_country': ship_country,
                    }
        url = 'https://api.fraudlabspro.com/v1/order/screen'
        data = urllib.parse.urlencode(validate_variable_list)
        data = data.encode('utf-8')
        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
            string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        result = json.dumps(json_obj, indent=4)
        if result is None:
            return False
        return(result)
    
    """
     # Sends decision back to FraudLabs Pro.
     #
     # Result will be return in json format.
    """
    def feedback(feedback_variables):
        if 'key' in feedback_variables:
            apikey = feedback_variables['key']
        else:
            return 'The API key is required. Please obtain through here: https://www.fraudlabspro.com/pricing'
        if 'id' in feedback_variables:
            transaction_id = feedback_variables['id']
        else:
            return 'Your ID is empty!'
        if 'action' in feedback_variables:
            action = feedback_variables['action']
        else:
            return 'Please choose your action.'
        if 'notes' in feedback_variables:
            notes = feedback_variables['notes']
        else:
            notes = ''
        feedback_variables_list = {
            'key': apikey,
            'format': 'json',
            'id': transaction_id,
            'action': action,
            'notes': notes,
        }
        url = 'https://api.fraudlabspro.com/v1/order/feedback'
        data = urllib.parse.urlencode(feedback_variables_list)
        data = data.encode('utf-8')
        request = urllib.request.Request(url, data)
        with urllib.request.urlopen(request) as response:
            string = response.read().decode('utf-8')
        json_obj = json.loads(string)
        result = json.dumps(json_obj, indent=4)
        if result is None:
            return False
        return(result)

    """
     # Gets transaction result.
     #
     # Result will be return in json format.
    """
    def get_transaction(get_transaction_variables):
        if 'key' in get_transaction_variables:
            api_key = get_transaction_variables['key']
        else:
            return('The API key is required. Please obtain through here: https://www.fraudlabspro.com/pricing')
        if 'id' in get_transaction_variables:
            fraud_labs_pro_id = get_transaction_variables['id']
        else:
            return "Your ID is empty!"
        if 'id_type' in get_transaction_variables:
            id_type = get_transaction_variables['id_type']
        else:
            return "Your ID type is empty!"
        get_transaction_variable_list = {
            'key': api_key,
            'format': 'json',
            'id': fraud_labs_pro_id,
            'id_type': id_type,
        }
        url = 'https://api.fraudlabspro.com/v1/order/result'
        url_values = urllib.parse.urlencode(get_transaction_variable_list)
        full_url = url + '?' + url_values
        data = urllib.request.urlopen(full_url)
        string = data.read().decode('utf-8')
        json_obj = json.loads(string)
        result = json.dumps(json_obj, indent=4)
        if result is None:
            return False
        return(result)

