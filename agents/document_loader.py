from langchain.agents import create_agent
from langchain_mcp_adapters.client import MultiServerMCPClient
from schemas.state import RequirementState
from config.llm_config import get_llm_config

llm = get_llm_config("ollama", "gemma4:e2b")

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

        print("============== file content loading started ==============")

        result = await agent.ainvoke({
            "messages": [
                {
                    "role": "user",
                    "content": f"""
                        Get the content of the file with file name contains {state["file_name"]}.
                    """
                }
            ]
        })

        state["raw_text"] = result["messages"][-1].content

        print("================== content downloaded ==============")

        return state