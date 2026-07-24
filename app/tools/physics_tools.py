import math
from pydantic_ai import RunContext
from app.tools.math_tools import quadratic_solver

# Debug function
def debug():
	"""
	Function to print debug statment to screen to insure agent is using tools
	"""
	return print("Tool called!")


def calculating_time_from_velocity(initial_velocity: float, final_velocity: float, acceleration: float) -> float:
	""" 
		Use this tool whenever you need to determine how long it takes for an object's velocity to change to a specified value.
		Using the following equation:
							t = (v_f - v_i) / a 

		Examples:
			- A ball thrown upward reaches maximum height
		  		-final_velocity = 0

			- A car slows from 20 m/s to 0 m/s

			- An object accelerates from rest to 15 m/s


		Arguments: 
			initial_velocity: Initial velocity in m/s
			final_velocity: Final velocity in m/s
			gravity: Acceleration due to gravity in m/s^2


		Returns:
			Time to reach final velocity in seconds
	"""

	# Debug line to see if model actually uses tool
	debug()

	if acceleration == 0:
		raise ValueError("Acceleration cannot be zero.")
	
	return (final_velocity - initial_velocity) / acceleration


def calculating_final_velocity(initial_velocity: float, time: float, acceleration: float) -> float:
	"""
		Use this tool whenever you need to determine the final velocity of an object under constant acceleration after a certain amount of time.
		Using the following equation:
								v_f = v_i + a*t

		Examples: 
		- Ball drops in the air for 4 seconds
			-initial_velocity=0
		- Car decelerates for 1.5 seconds
		- Airplane accelerates from rest for 200 seconds
			-initial_velocity=0

		Arguments:
			initial_velocity: Initial velocity in m/s
			time: time under acceleration in seconds
			acceleration: Acceleration or deceleration in m/s^2

		Returns:
			final velocity after a certain period under constant acceleration
	"""

	# Debug
	debug()

	return initial_velocity + acceleration * time


def calculating_displacement(initial_velocity: float, time: float, acceleration: float) -> float:
	"""
		Use this tool to calculate the horizontal or vertical displacement of an object under constant acceleration after a specific period of time
		Using the following equation: 
							dx = v_i * t + 1/2 * a * t^2

		Examples:
			- How far does a ball fall after 2 seconds
				- initial_velocity=0
			- Car traveling at 50 mph accelerating at 2mph^2 for 30 seconds
			- Man decelerating from 3.5 m/s at 0.25 m/s^2 in 2 seconds
			- Arrow shot out of bow at 30m/s upward in air after 10 seconds

		Arguments:
			initial_velocity: Initial velocity in m/s
			time: period of time for movement in seconds
			acceleration: acceleration or deceleration in m/s^2

		Returns:
			Horizontal or vertical displacement of object
	"""

	# Debug
	debug()

	return initial_velocity * time + 0.5 * acceleration * time**2


def calculating_initial_velocity_from_displacement(final_velocity: float, acceleration: float, displacement: float) -> float:
	"""
		Use this tool to calculate the initial velocity of an object using the final velocity, acceleration, and displacement.
		Use the following equation: 
							v_i = sqrt(v_f^2 - 2*a*dx)

		Examples:
			-Find the initial velocity of a thrown ball
			-Determine the launch speed of an arrow

		Arguments:
			final_velocity: Final velocity in m/s
			acceleration: Constant acceleration in m/s^2
			displacement: Displacement in meters

		Returns:
			Initial velocity in m/s
	"""

	# Debug
	debug()

	radicand = final_velocity**2 - 2 * acceleration * displacement

	if radicand < 0:
	    raise ValueError(
	        "No real initial velocity exists for the given inputs."
	    )

	return math.sqrt(radicand)


def calculating_final_velocity_from_displacement(initial_velocity: float, acceleration: float, displacement: float) -> float:
	"""
		Use this tool to calculate the final velocity of an object using the initial velocity, acceleration, and displacement.
		Use the following equation: 
							v_f = sqrt(v_i^2 + 2*a*dx)

		Examples:
			-Find the final velocity
			-Determine the speed of an arrow after a known distance

		Arguments:
			initial_velocity: Initial velocity in m/s
			acceleration: Constant acceleration in m/s^2
			displacement: Displacement in meters

		Returns:
			Final velocity in m/s
	"""

	# Debug
	debug()

	radicand = initial_velocity**2 + 2 * acceleration * displacement

	if radicand < 0:
	    raise ValueError(
	        "No real final velocity exists for the given inputs."
	    )

	return math.sqrt(radicand)


def calculating_time_from_displacement(initial_velocity: float, acceleration: float, displacement: float):
	"""
		Use this tool to calculate the time required to travel a given displacement with specific initial velocity and acceleartion
		Using the following equation:
							0 = 0.5 * a * t^2 + v_i * t - dx

		Examples:
			- find the time required to travel a given displacement
			- determine possible times an object takes to reach a position

		Arguments:
	        initial_velocity: Initial velocity in m/s
	        acceleration: Constant acceleration in m/s²
	        displacement: Displacement in meters

    	Returns:
        	Dictionary containing the possible time solution(s) in seconds.
	"""

	# Debug
	debug()

	a = 0.5*acceleration
	b = initial_velocity
	c = -1 * displacement

	return quadratic_solver(a, b, c)






