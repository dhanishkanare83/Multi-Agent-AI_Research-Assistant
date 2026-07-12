from agents.merge_agent import merge_agent

research = """
AI helps improve crop monitoring using drones.
Precision agriculture increases productivity.
"""

news = """
New AI robots are being deployed in farms.
The AI agriculture market is growing rapidly.
"""

result = merge_agent(research, news)

print(result)