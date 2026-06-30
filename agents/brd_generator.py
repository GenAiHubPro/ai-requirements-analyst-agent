from langchain.agents import create_agent

from schemas.state import RequirementState
from config.llm_config import llm

system_prompt = """
    You are a Senior Business Analyst.
    
    Your responsibility is to prepare a professional Business Requirements Document (BRD).
    
    The requirements are available at state as raw_text and the final classified information is available in state as classified_requirements.
        
    Use only the validated requirements provided in the workflow state.
    
    DO not invent requirements
    
    Do not assume missing information
    
    If unresolved gaps still exists, include them under an "Open Issues" section.
    
    Generate the following sections:
    
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
        
    Return the result in Markdown format.
    
"""

agent = create_agent(
    model=llm,
    system_prompt=system_prompt,
    name="BRDAgent"
)

class BRDAgent:
    async def __call__(self, state: RequirementState) -> RequirementState:
        return await self.invoke(state)

    async def invoke(self, state: RequirementState) -> RequirementState:

        print("================== brd document generation started ====================")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"The classified requirements are: {state.get("classified_requirements")}"
                }
            ]
        })

        state["brd_document"] = result["messages"][-1].content

        print("================== brd document generated ====================")

        return state