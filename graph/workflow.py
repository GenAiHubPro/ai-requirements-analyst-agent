from langgraph.graph import StateGraph, START, END
from schemas.state import RequirementState

from agents.document_loader import LoaderAgent
from agents.summarizer import SummarizerAgent

builder = StateGraph(RequirementState)

builder.add_node("loader", LoaderAgent())
builder.add_node("summarizer", SummarizerAgent())

builder.add_edge(START, "loader")
builder.add_edge("loader", "summarizer")
builder.add_edge("summarizer", END)


graph = builder.compile()