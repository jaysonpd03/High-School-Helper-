import math
from pydantic_ai import RunContext

# Debug function
def debug():
	"""
	Function to print debug statment to screen to insure agent is using tools
	"""
	return print("Tool called!")


def addition(x: float, y: float) -> float:
	"""
	Tool to calculate the addition of two numbers

	Use this tool whenever the user asks:
		- x + y
		- What is x plus y?
		- x + (-y)
		
	Arguments:
		x: a real number 
		y: a real number

	Returns:
		The summation of two real numbers
	"""
	# Debug
	debug()

	return x + y


def subtraction(x: float, y: float) -> float:
	"""
	Tool to calculate the subtraction of two real numbers

	Use this tool when the users asks:
	- x - y
	- What is x minus y
	- What is x subtracted by y
	- x - (-y)
	- What is the difference between x and y

	Arguments:
		x: a real number
		y: a real number

	Returns:
		The result of a number subtracted by another
	"""

	# Debug
	debug()

	return x - y


def multiplication(a: float, b: float) -> float:
	"""
	Tool to calculate the multiplication of two numbers

	Use this tool whenever the user asks:
		- a * b
		- What is a times b?
		- What is a multiplied by b?
		- a * (-b)
		- a x b
		- What is the product of a and b?
		
	Arguments:
		a: a real number 
		b: a real number

	Returns:
		The product of two real numbers
	"""
	# Debug
	debug()

	return a * b


def division(a: float, b: float) -> float:
	"""
	Tool to calculate the division of two real numbers

	Use this tool when the users asks:
	- a / b
	- What is a divided by b
	- What is the quotient of a and b
	- a / (-b)

	Arguments:
		a: a real number
		b: a real number

	Returns:
		The quotient of two real numbers 
	"""

	# Debug
	debug()

	return a / b


def square_root(value: float) -> float:
	"""
	 Calculate the square root of a non-negative number

	 Arguments:
	 	value: The number to find the square root of 

	 Returns:
	 	The square root of value
	"""
	# Debug line to see if agent actually uses tool
	debug()

	if value < 0:
		raise ValueError("Square root is only defined for non-negative numbers.")

	return math.sqrt(value)


def quadratic_solver(a: float, b: float, c: float):
	"""
	Solve a quadratic equation using the quadratic formula

	Arguments:
		a: coefficient of x^2
		b: coefficient of x
		c: constant (non-variable term)

	Returns: 
		dictionary of roots/solutions
	"""

	# Debug line
	debug()

	# Check to see if equation is quadratic
	if a==0:
		raise ValueError("Equation is not quadratic.")

	# Discriminant check to see where solution lies and best course to solve
	discriminant = b**2 - 4*a*c
	if discriminant > 0:
		root1 = (- b + math.sqrt(discriminant)) / (2*a)
		root2 = (- b - math.sqrt(discriminant)) / (2*a)

		return { 
					"discriminant": discriminant,
					"root1": root1, 
					"root2": root2,
					"nature": "two real solutions"
				}
	elif discriminant < 0:
		return { 
					"discriminant": discriminant,
					"root1": None,
					"root2": None,
					"nature": "two complex solutions"
				}
	else:
		root = - b / (2*a)
		return { 
					"discriminant": discriminant,
					"root1": root, 
					"root2": root,
					"nature": "One repeated real solution"
				}


def calculate_exponent(base: float, exponent: float) -> float:
	"""
	Function to compute exponentiation

	Use this tool whenever a user asks to:
	- evaluate expressions like 2^3
	- calculate powers
	- compute exponents
	- raise one number to another power

	Examples:
		2^3
		10 to the power of 4
		7 raised by -2
		16**2
		(-3) to the second power
		36^0.5
	
	Arguments:
		base: base number or number being raised
		exponent: the exponent or power

	Returns:
		Result of base raised to the exponent
	"""

	# Debug
	debug()

	return base ** exponent


def absolute_value(number: float) -> float:
	"""
		Compute the absolute value of a number

		Use this tool when needing to:
			- Find the distance from zero
			- Remove a negative sign
			- evaluate |x|
			- compute an absolute value

		Arguments:
			number: any real number

		Returns:
			Non-negative absolute value of the number
	"""

	# Debug
	debug()

	return abs(number)


def calculate_factorial(number: float) -> float:
	"""
		This tool calculates the factorial of a non-negative integer 

		Use this tool when the user asks:
		- Evaluate x!
		- What is the factorial of 4
		- Evaluate -x!
		- 3.5!

		Arguments:
			number: the base number for the factorial

		Returns:
			The results of factorial multiplication
	"""

	# Debug
	debug()

	# Check if non-negative
	if number < 0:
		raise ValueError("Factorials are only defined for non-negative integers")

	# Check if an integer
	if not number.is_integer():
		raise ValueError("Factorials are only defined for integers")

	return math.factorial(int(number))



