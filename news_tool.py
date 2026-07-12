from dotenv import load_dotenv
from langchain_tavily import TavilySearch

load_dotenv()

news_tool = TavilySearch(max_results=5)

def search_news(query: str):
    return news_tool.invoke(f"Latest news about {query}")