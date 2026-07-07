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



from langchain.agents import create_agent
from schemas.state import RequirementState
from config.llm_config import get_llm_config
import os
import logging

llm = get_llm_config(os.getenv("MODEL_PROVIDER"), os.getenv("MODEL_NAME"))

system_prompt = """
    You are a senior business analyst.
    
    Read the content of the requirement document provided by the user

    Generate:
        - Business Summary
        - Actors
        - Business Goals
        - Pain points
        - Current workflow
        - expected workflow
        - Business rules
        - dependencies
        - risks

    Returns the response as JSON format 
"""

agent = create_agent(
    model=llm,
    tools=[],
    name="SummarizerAgent",
    system_prompt=system_prompt
)

class SummarizerAgent:

    async def __call__(self, state: RequirementState):
        return await self.invoke(state)
    
    async def invoke(self, state: RequirementState) -> RequirementState:

        logger = logging.getLogger(__name__)

        logger.info("Summarizer initiated")

        document = state["raw_text"]

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": document
                }
            ]
        })

        state["summary"] = result["messages"][-1].content

        logger.info("summary ready and updated in the state")

        return state