from agents.researcher import researcher_agent
from agents.writer import writer_agent

question = "Latest AI trends in Agriculture"

research_notes = researcher_agent(question)

report = writer_agent(research_notes)

print(report)