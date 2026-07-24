from app.agent import agent

result = agent.run_sync("Evaluate -3!")

print(result.output)