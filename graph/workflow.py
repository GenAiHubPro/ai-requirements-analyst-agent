from langgraph.graph import StateGraph, START, END
from schemas.state import RequirementState

from agents.document_loader import LoaderAgent
from agents.summarizer import SummarizerAgent
from agents.classifier import ClassifierAgent
from agents.gap_analysis import GapAnalysisAgent
from agents.brd_generator import BRDAgent

builder = StateGraph(RequirementState)

builder.add_node("DocumentLoaderAgent", LoaderAgent())
builder.add_node("SummarizerAgent", SummarizerAgent())
builder.add_node("ClassifierAgent", ClassifierAgent())
builder.add_node("GapAnalysisAgent", GapAnalysisAgent())
builder.add_node("BRDAgent", BRDAgent())

builder.add_edge(START, "DocumentLoaderAgent")
builder.add_edge("DocumentLoaderAgent", "SummarizerAgent")
builder.add_edge("SummarizerAgent", "ClassifierAgent")
builder.add_edge("ClassifierAgent", "GapAnalysisAgent")
builder.add_edge("GapAnalysisAgent", "BRDAgent")
builder.add_edge("BRDAgent", END)


graph = builder.compile()