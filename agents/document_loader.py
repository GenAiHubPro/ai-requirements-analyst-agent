from langchain_ollama import ChatOllama
from langchain.agents import create_agent
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient
from schemas.state import RequirementState


llm = ChatOllama(
    model="gemma4:e2b",
    temperature=0
)

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
        return await self.invoke(state)

    async def invoke(self, state: RequirementState) -> RequirementState:

        print("========= loader agent initiated ========")

        tools = await client.get_tools()

        print("=========== Tools received from mcp sever to connect with google drive ================")

        agent = create_agent(
            model=llm,
            name="DocumentLoaderAgent",
            tools=tools,
            system_prompt="""
            Perform the operations againt the google drive based on user query. if requried use available tools to achieve the task
            """
        )

        print("========= downloading file content =========")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                        Read {state["file_name"]}.
                    """
                }
            ]
        })

        print("======== file content downloaded =========")

        state["raw_text"] = result["messages"][-1].content

        return state