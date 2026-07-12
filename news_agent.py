from llm import llm
from prompts.news_prompt import news_prompt
from tools.news_tool import search_news

news_chain = news_prompt | llm


def news_agent(question: str):

    news = search_news(question)

    response = news_chain.invoke(
        {
            "news": news
        }
    )

    return response.content