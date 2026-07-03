import asyncio

from graph.workflow import graph

async def main():

    state = {
        "file_name": "Requirements.docx",
        "raw_text": "",
        "summary": {},
        "classified_requirements": [],
        "gap_analysis": [],
        "brd_document": ""
    }

    result = await graph.ainvoke(state)

    print(f"The final result is: {result['brd_document']}")

    print("=================== THE END =================")

if __name__ == "__main__":
    asyncio.run(main())