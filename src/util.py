"""This is a utility module with helper functions that support 
the clocker class"""

import math

def round_two_decimals(float_number):
	"""Take a floating point number and round it to two decimal places"""
	return math.ceil(float_number*100)/100

def round_three_decimals(float_number):
	"""Take a floating point number and round it to two decimal places"""
	return math.ceil(float_number*1000)/1000