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

from core.abstractions import DocumentSource
from core.base_agent import BaseAgent
from prompts.system_prompts import LOADER_AGENT_SYSTEM_PROMPT
from schemas.state import RequirementState


class LoaderAgent(BaseAgent):
    name = "DocumentLoaderAgent"

    def __init__(self, llm, document_source: DocumentSource):
        super().__init__(llm)
        self.document_source = document_source
        self.agent = create_agent(
            model=self.llm,
            name=self.name,
            tools=[],
            system_prompt=LOADER_AGENT_SYSTEM_PROMPT,
        )

    async def run(self, state: RequirementState) -> RequirementState:
        content = await self.document_source.get_content(state["file_name"])
        state["raw_text"] = content
        return state
