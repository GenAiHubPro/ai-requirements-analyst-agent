from langchain.agents import create_agent
from schemas.state import RequirementState
from config.llm_config import get_llm_config

llm = get_llm_config("ollama", "gemma4:e2b")

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

        print("======= summarizer initiated =======")

        document = state["raw_text"]

        print("=========== content received from loader agent and summarization started =========")
        print(document)

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": document
                }
            ]
        })

        state["summary"] = result["messages"][-1].content

        print("============ summary ready and updated in the state ==============")

        return state