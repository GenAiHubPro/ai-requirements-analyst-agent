from langchain.agents import create_agent
from schemas.state import RequirementState
from config.llm_config import get_llm_config

llm = get_llm_config("ollama", "gemma4:e2b")

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

        print("==================== The gap analysis task is started ======================")

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

        print("================ The gap analysis task is done =====================")

        return state