from agents.researcher import researcher_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent

question = "Latest AI trends in Agriculture"

research = researcher_agent(question)

draft = writer_agent(research)

final_report = reviewer_agent(draft)

print(final_report)