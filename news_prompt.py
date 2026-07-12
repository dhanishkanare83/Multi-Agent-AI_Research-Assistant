from langchain_core.prompts import ChatPromptTemplate

news_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are an AI News Research Agent.

Your task is to summarize the latest news.

Write concise research notes.

Include:

- Latest News
- Important Developments
- Key Highlights

Keep the response under 200 words.
"""
        ),
        (
            "human",
            "{news}"
        )
    ]
)