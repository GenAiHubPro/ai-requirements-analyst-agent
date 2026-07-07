# Copyright (C) 2026 Jagadeeswara Rao Patta
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.

import asyncio
from graph.workflow import graph
from dotenv import load_dotenv
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    force=True,  # Python 3.8+
)

load_dotenv()

async def main():

    state = {
        "file_name": "Requirements.docx",
        "raw_text": "",
        "summary": {},
        "classified_requirements": [],
        "gap_analysis": [],
        "brd_document": "",
        "functional_specifications": "",
        "user_stories": [],
    }

    result = await graph.ainvoke(state)

    print(f"The final result is: {result['user_stories']}")

    print("=================== THE END =================")

if __name__ == "__main__":
    asyncio.run(main())
