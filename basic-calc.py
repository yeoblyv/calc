#Basic 2-number Calculator Functions
def add(x,y):
	pass

def multiply(x,y):
	return x*y

def subtract(x,y):
	pass

def divide(x,y):
	"""
	This function divides two numbers and returns the result.
	It takes two parameters, x and y.
	
	Inputs:
		x : int or float
		y : int or float

	Returns:
		float : The result of dividing x by y.
	"""
	return print(f"the result of {x}/{y} is {x/y}")

def power(x,y):
	"""
	This function raises a number to the power of another number and returns the result.
	It takes two parameters, x and y.
	
	Inputs:
		x : int or float
		y : int or float
	"""
	return x**y

def factorial(n):
	"""
	This function calculates the factorial of a number and returns the result.
	It takes one parameter, n.
	
	Inputs:
		n : int
		Returns:
		int : The factorial of n.
	"""
	if n == 0:
		return 1
	else:
		return n * factorial(n-1)	