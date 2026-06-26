from langchain.agents import create_agent
from langchain.tools import tool
from langchain_ollama import ChatOllama
from schemas.state import RequirementState


llm = ChatOllama(
    model="gemma4:e2b",
    temperature=0
)


system_prompt = """
    You are a senior business analyst.
    Read the content of the requriement document provided by the DocumentLoaderAgent

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

    Returns the abvove details as JSON format 
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