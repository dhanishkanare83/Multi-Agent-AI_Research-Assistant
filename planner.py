from llm import llm
from prompts.planner_prompt import planner_prompt

planner_chain = planner_prompt | llm


def planner_agent(question: str):
    response = planner_chain.invoke(
        {
            "question": question
        }
    )

    return response.content