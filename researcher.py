from llm import llm
from prompts.researcher_prompt import research_prompt
from tools.search_tool import search_web

research_chain = research_prompt | llm


def researcher_agent(question: str):
    # Get web search results
    results = search_web(question)

    # Generate research notes
    response = research_chain.invoke(
        {
            "question": question,
            "search_results": results
        }
    )

    return response.content