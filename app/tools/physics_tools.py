


def time_to_max_height(initial_velocity: float, gravity: float=9.8) -> float:
	""" 
	Calculate the time required for an object with an upward velocity to reach maximum height.

	Arguments: 
		initial_velocity: Initial upward velocity in m/s
		gravity: Acceleration due to gravity in m/s^2


	Returns:
		Time to reach maximum heigh in seconds
	"""

	# Debug line to see if model actually uses tool
	# print("Tool called!") 

	if gravity <= 0:
		raise ValueError("Gravity must be positive.")

	return initial_velocity / gravity