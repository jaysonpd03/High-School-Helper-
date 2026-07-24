from app.agent import agent

result = agent.run_sync("Use the calculate_exponent tool to evaluate 17^23")

print(result.output)