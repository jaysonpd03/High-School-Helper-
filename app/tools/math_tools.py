import math
from pydantic_ai import RunContext

# Debug function
def debug():
	"""
	Function to print debug statment to screen to insure agent is using tools
	"""
	return print("Tool called!")


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



