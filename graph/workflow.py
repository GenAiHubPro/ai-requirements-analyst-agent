# Copyright (C) 2026 Jagadeeswara Rao Patta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
import os

from langgraph.graph import StateGraph, START, END
from psycopg import AsyncConnection
from psycopg.rows import dict_row

from core.base_agent import BaseAgent
from schemas.state import RequirementState
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver


async def build_graph(agents: dict[str, BaseAgent]):
    """Build the workflow from an injected, ordered agent registry (OCP).

    The execution order is the dict insertion order, so adding/reordering
    a step is done purely by changing the passed dict in the composition
    root (``main.py``) — this module is never edited to extend the pipeline.
    """
    builder = StateGraph(RequirementState)

    for node_name, agent in agents.items():
        builder.add_node(node_name, agent)

    node_names = list(agents.keys())
    if not node_names:
        raise ValueError("Cannot build graph: no agents provided")

    builder.add_edge(START, node_names[0])
    for current, nxt in zip(node_names, node_names[1:]):
        builder.add_edge(current, nxt)
    builder.add_edge(node_names[-1], END)

    conn = await AsyncConnection.connect(
        os.getenv("DB_URL"),
        autocommit=True,
        prepare_threshold=0,
        row_factory=dict_row,
    )
    checkpointer = AsyncPostgresSaver(conn=conn)
    await checkpointer.setup()
    return builder.compile(
        checkpointer=checkpointer,
        interrupt_before=["GapAnalysisAgent"]
    )
