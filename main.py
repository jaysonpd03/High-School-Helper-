from app.agent import agent

prompt="If I throw a ball out a window that is 30 feet off of the ground at 10 miles per hour, how far from the building will the ball hit the ground assuming no air resistance?"
print("Question: " + prompt + "\n")
result = agent.run_sync(prompt)

print(result.output)