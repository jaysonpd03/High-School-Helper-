from app.agent import agent

result = agent.run_sync("A ball is thrown upward on Mars with an initial velocity of 30 m/s. How long until it stops rising? Mars has a gravity of g=3.721 m/s^2")

print(result.output)