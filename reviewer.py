from llm import llm
from prompts.reviewer_prompt import reviewer_prompt

reviewer_chain = reviewer_prompt | llm


def reviewer_agent(report: str):
    response = reviewer_chain.invoke(
        {
            "report": report
        }
    )

    return response.content