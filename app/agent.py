from pydantic_ai import Agent
from pydantic_ai.models.ollama import OllamaModel
from pydantic_ai.providers.ollama import OllamaProvider

from app.tools.math_tools import square_root
from app.tools.physics_tools import time_to_max_height

# What model is the agent using?
model = OllamaModel("qwen3:1.7b", provider=OllamaProvider(base_url="http://localhost:11434/v1"), )

# Defining the agent
agent = Agent(
	model, 
	system_prompt="""
	You are a helpful high school math and physics tutor. Use tools whenever calculations are required. 
	Explain your reasoning clearly and precisely so students can better understand. 

	""", 

	# Library of 'tools' for agent to use
	tools=[square_root, time_to_max_height]

	)
