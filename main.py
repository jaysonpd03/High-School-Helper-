from app.agent import agent

result = agent.run_sync("Solve the following problems: 1. x^2 - 4x + 4=0 2. x^2 + 2x + 5=0 3. 2x^2 + 7x - 4=0 4. 5x + 3=0")

print(result.output)