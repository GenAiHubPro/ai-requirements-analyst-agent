from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from schemas.state import RequirementState
from config.llm_config import llm

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

        tools = await client.get_tools()

        agent = create_agent(
            model=llm,
            name="DocumentLoaderAgent",
            tools=tools,
            system_prompt="""
                As a Document Loader.
                
                Get the document of given filename from the google drive.
                
                Return the content of the file as it is. without doing any changes in the file content
            """
        )

        print("============== file content loading started ==============")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                        Get all available files with file name contains {state["file_name"]}.
                    """
                }
            ]
        })

        state["raw_text"] = result["messages"][-1].content

        print("================== content downloaded ==============")

        return state