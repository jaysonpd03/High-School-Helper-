from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from app.tools.math_tools import square_root, quadratic_solver, calculate_exponent
from app.tools.physics_tools import time_to_max_height

# What model is the agent using?
model = OllamaModel("qwen3:1.7b", provider=OllamaProvider(base_url="http://localhost:11434/v1"), )

# Defining the agent (Who is the agent?)
agent = Agent(
	model, 
	system_prompt="""
	You are a helpful high school math and physics AI tutor. Always use tools whenever calculations are required. 
	Explain your reasoning clearly and precisely so students can better understand. 

	Your goals are to help students understand concepts, not just give them the answer. Explain and show equations and reasoning behind the equation.
	Explain results in an appropriate manner for a high school student to follow your decisions and execution.

	When solving a problem walk through steps that mirror how a student should tackle a problem:
	1. Identify the type of problem in front of you and relevant concepts. 
	2. Determine the tools that would be useful.
	3. Execute the calculations using the tools.
	4. Explain the step-by-step solution how a student would show their work. 

	""", 

	# Library of 'tools' for agent to use
	tools= [
			square_root, 
			time_to_max_height,
			quadratic_solver,
			calculate_exponent


			]

	)
