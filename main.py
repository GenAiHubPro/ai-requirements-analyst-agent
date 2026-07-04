import asyncio
from graph.workflow import graph
from dotenv import load_dotenv

load_dotenv()

async def main():

    state = {
        "file_name": "Requirements.docx",
        "raw_text": "",
        "summary": {},
        "classified_requirements": [],
        "gap_analysis": [],
        "brd_document": "",
        "functional_specifications": ""
    }

    result = await graph.ainvoke(state)

    print(f"The final result is: {result['functional_specifications']}")

    print("=================== THE END =================")

if __name__ == "__main__":
    asyncio.run(main())