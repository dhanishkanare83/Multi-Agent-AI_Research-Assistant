from tavily import TavilyClient
from dotenv import load_dotenv
import os

load_dotenv()

client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def search_papers(query: str):
    result = client.search(
        query=f"{query} research papers",
        max_results=5
    )

    return result