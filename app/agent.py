from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from app.tools.math_tools import addition, subtraction, multiplication, division, square_root, quadratic_solver, calculate_exponent, absolute_value, calculate_factorial
from app.tools.physics_tools import calculating_time_from_velocity, calculating_final_velocity, calculating_displacement, calculating_initial_velocity_from_displacement, calculating_final_velocity_from_displacement, calculating_time_from_displacement

# What model is the agent using?
model = OllamaModel("qwen3:1.7b", provider=OllamaProvider(base_url="http://localhost:11434/v1"), )

# Defining the agent (Who is the agent?)
agent = Agent(
	model, 
	system_prompt="""
	You are a helpful high school math and physics AI tutor. You have access to specialized calculations tools. 
	Explain your reasoning clearly and precisely so students can better understand. 

	Your goals are to help students understand concepts, not just give them the answer. Explain and show equations and reasoning behind the equation.
	Explain results in an appropriate manner for a high school student to follow your decisions and execution.

	When solving a problem walk through steps that mirror how a student should tackle a problem:
	1. Identify the type of problem in front of you and relevant concepts. 
	2. Determine the tools matches the required calculation.
	3. Execute the calculations using the tools.
	4. Explain the step-by-step solution how a student would show their work. 

	Rules:
	- Never perform arithmetic yourself
	- Never evaluate equations yourself
	- Whenever a numerical answer is required, you MUST call the appropriate tool. 
	- Only explain the calculation after the tool returns a result.
	- If multiple calculations are needed, call the appropriate tool for each one. 

	If you encounter a problem that you do not have tool for then explain to the student that you don't have a tool for the question. 
	If this happens recommend the student a guideline on how to solve the problem but do not perform any calculations. 
	Explicitly state that you are only providing guidance for solving the problem. 

	""", 

	# Library of 'tools' for agent to use
	tools= [
			addition,
			subtraction,
			multiplication,
			division,
			square_root, 
			quadratic_solver,
			calculate_exponent,
			absolute_value,
			calculate_factorial,
			calculating_time_from_velocity, 
			calculating_final_velocity,
			calculating_displacement, 
			calculating_initial_velocity_from_displacement,
			calculating_final_velocity_from_displacement,
			calculating_time_from_displacement
			]

	)
