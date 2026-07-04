from langchain.agents import create_agent

from schemas.state import RequirementState
from config.llm_config import get_llm_config
import os
from langchain_mcp_adapters.client import MultiServerMCPClient

client = MultiServerMCPClient(
    {
        "google_drive": {
            "transport": "streamable_http",
            "url": "http://localhost:8000/mcp"
        }
    }
)

llm = get_llm_config(os.getenv("MODEL_PROVIDER"), os.getenv("MODEL_NAME"))

system_prompt = """

    You are a Senior Business Analyst. 
    
    Your primary responsibility is to prepare a professional Business Requirements Document (BRD).
    
    The requirements and the final classified information are provided by the user.
    
    CRITICAL RULES:
    1. Use ONLY the validated requirements provided by the user.
    2. DO NOT invent requirements or assume missing information.
    3. If unresolved gaps still exist, include them under an "Open Issues" section.
    
    BRD STRUCTURE:
    Generate the following sections exactly:
    1. Executive Summary
    2. Business Problem
    3. Business Objectives
    4. Project Scope
    5. Stakeholders
    6. Functional Requirements
    7. Non-Functional Requirements
    8. Business Rules
    9. Assumptions
    10. Constraints
    11. Dependencies
    12. Risks
    13. Success Criteria
    14. Open Issues
    
    TOOL EXECUTION STEP:
    Once the BRD text is fully formulated, you MUST execute the `create_markdown_file` tool before responding to the user.
    - Parameter 'file_path': Set this to "output/brd_document.md" (The directory name must be 'output').
    - Parameter 'title': Set to "Business Requirements Document (BRD)".
    - Parameter 'content': Insert the complete BRD text you generated.
    
    FINAL RESPONSE STEP:
    After the tool successfully executes and returns a success message, confirm to the user that the file was created and print the final BRD content in Markdown format for their review.

"""

class BRDAgent:
    async def __call__(self, state: RequirementState) -> RequirementState:
        return await self.invoke(state)

    async def invoke(self, state: RequirementState) -> RequirementState:

        print("================== brd document generation started ====================")

        tools = await client.get_tools()

        agent = create_agent(
            model=llm,
            system_prompt=system_prompt,
            name="BRDAgent",
            tools=tools
        )

        print(f" Tools: {tools}")

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

        state["brd_document"] = result["messages"][-1].content

        print("================== brd document generated ====================")

        return state