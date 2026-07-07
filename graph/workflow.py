# Copyright (C) 2026 Jagadeeswara Rao Patta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.


from langgraph.graph import StateGraph, START, END
from schemas.state import RequirementState

from agents.document_loader import LoaderAgent
from agents.summarizer import SummarizerAgent
from agents.classifier import ClassifierAgent
from agents.gap_analysis import GapAnalysisAgent
from agents.brd_generator import BRDAgent
from agents.functional_spec import FunctionalSpecificationAgent
from agents.user_story import UserStoryAgent

builder = StateGraph(RequirementState)

builder.add_node("DocumentLoaderAgent", LoaderAgent())
builder.add_node("SummarizerAgent", SummarizerAgent())
builder.add_node("ClassifierAgent", ClassifierAgent())
builder.add_node("GapAnalysisAgent", GapAnalysisAgent())
builder.add_node("BRDAgent", BRDAgent())
builder.add_node("FunctionalSpecificationAgent", FunctionalSpecificationAgent())
builder.add_node("UserStoryAgent", UserStoryAgent())

builder.add_edge(START, "DocumentLoaderAgent")
# builder.add_edge("DocumentLoaderAgent", END)
builder.add_edge("DocumentLoaderAgent", "SummarizerAgent")
builder.add_edge("SummarizerAgent", "ClassifierAgent")
builder.add_edge("ClassifierAgent", "GapAnalysisAgent")
builder.add_edge("GapAnalysisAgent", "BRDAgent")
builder.add_edge("BRDAgent", "FunctionalSpecificationAgent")
builder.add_edge("FunctionalSpecificationAgent", "UserStoryAgent")
builder.add_edge("UserStoryAgent", END)


graph = builder.compile()