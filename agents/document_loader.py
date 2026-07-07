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
from langchain_mcp_adapters.client import MultiServerMCPClient
from schemas.state import RequirementState
from config.llm_config import get_llm_config
import os
import logging

llm = get_llm_config(os.getenv("MODEL_PROVIDER"), os.getenv("MODEL_NAME"))

client = MultiServerMCPClient(
    {
        "google_drive": {
            "transport": "streamable_http",
            "url": "http://localhost:8000/mcp"
        }
    }
)

class LoaderAgent:

    async def __call__(self, state: RequirementState):
        if llm is None:
            raise Exception("AgenticException: LLM not available")
        return await self.invoke(state)

    async def invoke(self, state: RequirementState) -> RequirementState:

        tools = await client.get_tools()

        logger = logging.getLogger(__name__)

        agent = create_agent(
            model=llm,
            name="DocumentLoaderAgent",
            tools=tools,
            system_prompt="""
                As a Document Loader.
                
                Get the content of the document from the google drive. The document name Given by the user.
                
                Return use available tools if required to load the content and return the content to user without doing any changes
            """
        )

        logger.info("File content loading started")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                        Get the content of the file, with the file name must contains {state["file_name"]}.
                    """
                }
            ]
        })

        state["raw_text"] = result["messages"][-1].content

        logger.info("File content loading completed")

        return state