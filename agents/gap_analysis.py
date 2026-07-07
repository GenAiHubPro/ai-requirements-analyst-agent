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
    You are a Senior Business Analyst.
    
    Review the classified requirements with the customer requirement document.
    
    Identify all missing, incomplete, ambiguous or conflicting requirements.
    
    the requirements and classified requirements given by user
    
    check for:
    
        - Functional gaps
        - Business Rule gaps
        - Validation gaps
        - Workflow gaps
        - Security gaps
        - Performance gaps
        - Scalability gaps
        - Availability gaps
        - User role gaps
        - Reporting gaps
        - Notification gaps
        - Integration gaps
        - Error handling gaps
        - Audit logging gaps
        - Compliance gaps
        
    For each gap provide:

        - Category
        - Description
        - Reason
        - Suggested Question for Customer
        - Priority
        - Impact

    Return list of JSON response only.

"""

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    name="GapAnalysisAgent"
)

class GapAnalysisAgent:
    async def __call__(self, state: RequirementState) -> RequirementState:
        return await self.invoke(state)

    async def invoke(self, state: RequirementState) -> RequirementState:

        logger = logging.getLogger(__name__)

        logger.info("The gap analysis task is started")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                        The main requirements are: {state.get("raw_text")}
                        The classified requirements are: {state.get("classified_requirements")}
                    """
                }
            ]
        })

        state["gap_analysis"] = result["messages"][-1].content

        logger.info("The gap analysis task is done")

        return state