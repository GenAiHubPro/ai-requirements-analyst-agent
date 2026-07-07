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
    You are an experienced business Analyst.
    
    Analyze the requirements summary document provided by the user.
    
    For every requirement, identify:
    
        - Unique ID
        - Requirement Text
        - Requirement Category
        - Sub Category ( if possible )
        - Priority ( High / Medium / Low )
        - Confidence Score
        
    Valid categories are:
        
        - Functional Requirement
        - Non-Functional Requirement
        - Business RUle
        - Constraint 
        - Assumption
        - Risk
        - Dependency
        - Business Goal
        - Pain Point
        - Workflow
        - Validation Rule
        - Future enhancement
        - Out of scope
        - Open question
        
    Return the response as list of JSON only.
"""

agent = create_agent(
    model=llm,
    tools=[],
    name="ClassificationAgent",
    system_prompt=system_prompt,
)

class ClassifierAgent:

    async def __call__(self, state: RequirementState):
        return await self.invoke(state)

    async def invoke(self, state: RequirementState) -> RequirementState:

        logger = logging.getLogger(__name__)

        logger.info("classifier agent initialized")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": state.get("summary")
                }
            ]
        })

        state["classified_requirements"] = result["messages"][-1].content

        logger.info("The classification task is done")

        return state
