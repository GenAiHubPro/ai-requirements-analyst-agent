from langchain_ollama import ChatOllama
from langchain.agents import create_agent
import asyncio
from langchain_mcp_adapters.client import MultiServerMCPClient


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

async def main():

    tools = await client.get_tools()
    
    agent = create_agent(
        model=llm,
        tools=tools,
        system_prompt="""
        Perform the operations againt the google drive based on user query. if requried use available tools to achieve the task
        """
    )

    print(f"the tools are: {tools}")

    result = await agent.ainvoke({
        "messages": [
            {
                "role": "user",
                "content": """
                    Read Customer Requirement Document and summarize it.
                """
            }
        ]
    })

    for message in result["messages"]:
        print(message.content)
        
if __name__ == "__main__":
    asyncio.run(main())