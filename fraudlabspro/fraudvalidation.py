"""
 # FraudLabsPro Python Library
 # Implements fraud checking solution using FraudLabs Pro service.
 # API key is required, and if you do not have an API key, you may sign up free
 # at at https://www.fraudlabspro.com
 #
 # @copyright 2024-2026 FraudLabs Pro
 # https://www.fraudlabspro.com

"""
from .order import Order

# Legacy alias: FraudValidation is kept for backward compatibility. 
# It points to the Order class.
FraudValidation = Order