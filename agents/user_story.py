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
from prompts.system_prompts import USER_STORY_AGENT_SYSTEM_PROMPT
from schemas.state import RequirementState
from utils.response_utils import extract_text


class UserStoryAgent(BaseAgent):
    name = "UserStoryAgent"

    def __init__(self, llm):
        super().__init__(llm)
        self.agent = create_agent(
            model=self.llm,
            name=self.name,
            tools=[],
            system_prompt=USER_STORY_AGENT_SYSTEM_PROMPT,
        )

    async def run(self, state: RequirementState) -> RequirementState:
        result = await self.agent.ainvoke({
            "messages": [{
                "role": "user",
                "content": f"""
                    The Business Requirements Document (BRD) is: {state["brd_document"]},
                    The functional requirements are: {state["functional_specifications"]}
                """,
            }]
        })
        state["user_stories"] = extract_text(result["messages"][-1].content)
        return state
