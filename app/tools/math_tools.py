import math
from pydantic_ai import RunContext

def square_root(value: float) -> float:
	"""
	 Calculate the square root of a non-negative number

	 Arguments:
	 	value: The number to find the square root of. 

	 Returns:
	 	The square root of value
	"""
	# Debug line to see if agent actually uses tool
	# print("Tool called!")

	if value < 0:
		raise ValueError("Square root is only defined for non-negative numbers.")

	return math.sqrt(value)
