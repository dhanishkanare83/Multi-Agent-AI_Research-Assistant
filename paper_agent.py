from llm import llm
from langchain_core.prompts import ChatPromptTemplate

from tools.paper_tool import search_papers


paper_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an Academic Research Agent.

Your job is to read research paper search results and create a professional summary.

Return the report in this format:

Research Papers:
- Paper 1
- Paper 2
- Paper 3

Major Findings:
- ...
- ...

Latest Technologies:
- ...
- ...

Research Summary:
Provide a concise summary of the papers.
"""
        ),
        (
            "human",
            "{papers}"
        ),
    ]
)

paper_chain = paper_prompt | llm


def paper_agent(question: str):

    papers = search_papers(question)

    response = paper_chain.invoke(
        {
            "papers": str(papers)
        }
    )

    return response.content