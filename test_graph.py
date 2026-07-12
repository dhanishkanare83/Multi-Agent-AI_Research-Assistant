from graph.workflow import graph

initial_state = {
    "question": "Latest AI trends in Agriculture",
    "plan": "",
    "research": "",
    "news": "",
    "paper": "",
    "merged": "",
    "draft": "",
    "final": "",
    "need_research": False,
    "research_done": False,
    "news_done": False,
}

config = {
    "configurable": {
        "thread_id": "research-thread-1"
    }
}

result = graph.invoke(
    initial_state,
    config=config
)

print("\n========== FINAL REPORT ==========\n")
print(result)

print("\nReturned Keys:")
print(result.keys())