from llm import llm
from prompts.writer_prompt import writer_prompt

writer_chain = writer_prompt | llm


def writer_agent(research: str):
    response = writer_chain.invoke(
        {
            "research": research
        }
    )

    return response.content