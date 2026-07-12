from llm import llm
from langchain_core.prompts import ChatPromptTemplate

merge_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI Merge Agent.

You receive outputs from multiple research agents.

Combine them into one clean research document.

Requirements:
- Remove duplicate information.
- Keep all important facts.
- Organize logically.
- Produce concise research notes.
"""
        ),
        (
            "human",
            """
Web Research:

{research}

Latest News:

{news}
"""
        ),
    ]
)

merge_chain = merge_prompt | llm


def merge_agent(research, news, paper):

    response = merge_chain.invoke(
        {
            "research": research,
            "news": news,
        }
    )

    return response.content