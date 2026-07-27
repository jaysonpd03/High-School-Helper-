# High School Helper

An AI agent that solves high school math and physics problems using deterministic Python tools orchestrated by a local LLM through PydanticAI.

## Features

### Math Tools
- Addition
- Subtraction
- Multiplication
- Division
- Exponentiation
- Square Root
- Absolute Value
- Factorial
- Quadratic Equation Solver

### Physics Tools
Constant-acceleration kinematics including:

- Time from initial/final velocity
- Final velocity from time
- Displacement from time
- Initial velocity from displacement
- Final velocity from displacement
- Time from displacement

## Architecture

The project is organized into three primary components.

'''
app/
│
├── agent.py
│     Defines the AI agent, system prompt, and registers all tools.
│
├── tools/
│     Math and physics tool implementations.
│
└── main.py
      Simple interface for interacting with the agent.
'''

The agent uses:
- PydanticAI
- Ollama Qwen3 1.7b

Each mathematical or physics operation is implemented as an independent Python function that can be invoked by the language of the model


## Running the Project
Start an Ollama server
'''bash
ollama serve
'''

Run the application
'''bash
python main.py
'''

## Notes
This project was intentionally designed around small, reusable tools instead of creating dedicated functions for individual problems. The objective was to allow the model to identify the type of problem being solved, use an appropriate computation tool, and then generate a student-friendly explaination from the returned results. 
During development, I observed that the smaller model (1.7b) doesn't always use the tools when calculations are trivial for the model. However, the existing architecture allows the project to benefit from stonger models without requiring changes. 