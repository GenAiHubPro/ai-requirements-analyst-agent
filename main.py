import asyncio

from graph.workflow import graph

async def main():

    state = {
        "file_name": "Customer Requirement Document",
        "raw_text": "",
        "summary": ""
    }

    result = await graph.ainvoke(state)

    print(result["summary"] or "")

if __name__ == "__main__":

    asyncio.run(main())