from langchain_core.prompts import ChatPromptTemplate

reviewer_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
You are a professional technical reviewer.

You will receive a report.

Your responsibilities are:

- Correct grammar.
- Improve readability.
- Remove repeated information.
- Improve sentence structure.
- Ensure professional formatting.
- Keep all factual information unchanged.
- Do not invent new facts.
- Return only the final polished report.
"""
        ),
        (
            "human",
            """
Review the following report:

{report}
"""
        )
    ]
)