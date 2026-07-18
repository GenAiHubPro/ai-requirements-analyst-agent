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

from langchain.agents import create_agent

from core.base_agent import BaseAgent
from prompts.system_prompts import FUNCTIONAL_REQUIREMENTS_AGENT_SYSTEM_PROMPT
from schemas.state import RequirementState
from utils.response_utils import extract_text


class FunctionalSpecificationAgent(BaseAgent):
    name = "FunctionalSpecificationAgent"

    def __init__(self, llm):
        super().__init__(llm)
        self.agent = create_agent(
            model=self.llm,
            name=self.name,
            system_prompt=FUNCTIONAL_REQUIREMENTS_AGENT_SYSTEM_PROMPT,
        )

    async def run(self, state: RequirementState) -> RequirementState:
        result = await self.agent.ainvoke({
            "messages": [{
                "role": "user",
                "content": f"""
                    The requirement summary is: {state.get("summary")}
                    The classified requirements are: {state.get("classified_requirements")}
                    The Business Requirements Document content is: {state.get("brd_document")}
                    The Gap Analysis is: {state.get("gap_analysis")}
                """,
            }]
        })
        state["functional_specifications"] = extract_text(result["messages"][-1].content)
        return state
