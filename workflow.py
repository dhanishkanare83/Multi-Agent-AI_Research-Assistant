from agents.paper_agent import paper_agent
from typing import TypedDict, Literal

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import InMemorySaver

from agents.planner import planner_agent
from agents.researcher import researcher_agent
from agents.news_agent import news_agent
from agents.merge_agent import merge_agent
from agents.writer import writer_agent
from agents.reviewer import reviewer_agent


# =====================================================
# Shared State
# =====================================================

class ResearchState(TypedDict):
    question: str
    plan: str
    research: str
    news: str
    paper: str
    merged: str
    draft: str
    final: str
    need_research: bool

    research_done: bool
    news_done: bool


# =====================================================
# Planner Node
# =====================================================

def planner_node(state: ResearchState):

    print("\n========== Planner Agent ==========")

    plan = planner_agent(state["question"])

    state["plan"] = plan

    if "Research Required: YES" in plan:
        state["need_research"] = True
    else:
        state["need_research"] = False

    print(plan)

    return state


# =====================================================
# Research Node
# =====================================================

def research_node(state: ResearchState):

    print("\n========== Research Agent ==========")

    state["research"] = researcher_agent(state["question"])
    
    state["research_done"] = True

    return state


# =====================================================
# News Node
# =====================================================

def news_node(state: ResearchState):

    print("\n========== News Agent ==========")

    state["news"] = news_agent(state["question"])
    state["news_done"] = True

    return state


# =====================================================
# Merge Node
# =====================================================

def merge_node(state: ResearchState):

    print("\n========== Merge Agent ==========")

    state["merged"] = merge_agent(
    state["research"],
    state["news"],
    state["paper"]
)
    

    return state


# =====================================================
# Writer Node
# =====================================================

def writer_node(state: ResearchState):

    print("\n========== Writer Agent ==========")

    state["draft"] = writer_agent(state["merged"])

    return state


# =====================================================
# Reviewer Node
# =====================================================

def reviewer_node(state: ResearchState):

    print("\n========== Reviewer Agent ==========")

    state["final"] = reviewer_agent(state["draft"])

    return state


# =====================================================
# Router
# =====================================================

def route_after_planner(state: ResearchState) -> Literal["research", "writer"]:

    if state["need_research"]:
        print("\n➡️ Routing to Research Agent")
        return "research"

    print("\n➡️ Skipping Research Agent")
    return "writer"
def paper_node(state: ResearchState):

    print("\n========== Paper Agent ==========")

    state["paper"] = paper_agent(state["question"])

    return state

# =====================================================
# Build Graph
# =====================================================


# Register Nodes
builder = StateGraph(ResearchState)

builder.add_node("planner", planner_node)
builder.add_node("research", research_node)
builder.add_node("news", news_node)
builder.add_node("paper", paper_node)
builder.add_node("merge", merge_node)
builder.add_node("writer", writer_node)
builder.add_node("reviewer", reviewer_node)

# =====================================================
# Connect Nodes
# =====================================================





# =====================================================
# Edges
# =====================================================

builder.add_edge(START, "planner")

builder.add_conditional_edges(
    "planner",
    route_after_planner,
    {
        "research": "research",
        "writer": "writer",
    },
)

builder.add_edge("research", "news")
builder.add_edge("news", "paper")
builder.add_edge("paper", "merge")
builder.add_edge("merge", "writer")
builder.add_edge("writer", "reviewer")
builder.add_edge("reviewer", END)


# =====================================================
# Memory
# =====================================================

memory = InMemorySaver()


# =====================================================
# Compile
# =====================================================

graph = builder.compile(
    checkpointer=memory
)