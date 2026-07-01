from langchain.agents import create_agent
from schemas.state import RequirementState
from config.llm_config import llm

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

        print("=============== classifier agent initialized ================")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": state.get("summary")
                }
            ]
        })

        state["classified_requirements"] = result["messages"][-1].content

        print("============== The classification task is done =====================")

        return state