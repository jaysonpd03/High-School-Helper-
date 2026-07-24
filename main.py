from app.agent import agent

result = agent.run_sync("How far from zero is -5236?")

print(result.output)