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

import argparse
import asyncio
import logging
import os
import sys
import uuid

# Make the project root importable when run directly from any directory.
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import bootstrap  # noqa: F401  (ensures project root is importable from any CWD)

from dotenv import load_dotenv

from agents.brd_generator import BRDAgent
from agents.classifier import ClassifierAgent
from agents.document_loader import LoaderAgent
from agents.functional_spec import FunctionalSpecificationAgent
from agents.gap_analysis import GapAnalysisAgent
from agents.summarizer import SummarizerAgent
from agents.user_story import UserStoryAgent
from config.llm_config import get_llm_config
from graph.workflow import build_graph
from schemas.state import RequirementState
from tools.local_document_source import LocalDocumentSource
from tools.local_writer import LocalArtifactWriter

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    force=True,
)
logger = logging.getLogger("main")


# Central artifact persistence (DIP): the pipeline never relies on the LLM
# deciding to call a tool. Every artifact is written deterministically here.
ARTIFACT_FILES = {
    "summary": "RequirementSummary.md",
    "classified_requirements": "ClassifiedRequirements.md",
    "gap_analysis": "GapAnalysis.md",
    "brd_document": "BRD.md",
    "functional_specifications": "FunctionalSpecification.md",
    "user_stories": "UserStories.md",
}


async def main(file_name: str):
    load_dotenv()

    provider = os.getenv("MODEL_PROVIDER")
    model = os.getenv("MODEL_NAME")
    llm = get_llm_config(provider, model)  # raises clearly on bad provider

    # Composition root: concrete dependencies are assembled here and injected.
    document_source = LocalDocumentSource(input_dir="input")

    # One UUIDv4 per execution; all artifacts go under output/<execution_id>/.
    execution_id = str(uuid.uuid4())
    logger.info("Execution ID: %s", execution_id)
    writer = LocalArtifactWriter(base_dir="output", execution_id=execution_id)

    agents = {
        "DocumentLoaderAgent": LoaderAgent(llm, document_source),
        "SummarizerAgent": SummarizerAgent(llm),
        "ClassifierAgent": ClassifierAgent(llm),
        "GapAnalysisAgent": GapAnalysisAgent(llm),
        "BRDAgent": BRDAgent(llm),
        "FunctionalSpecificationAgent": FunctionalSpecificationAgent(llm),
        "UserStoryAgent": UserStoryAgent(llm),
    }

    graph = build_graph(agents)

    state: RequirementState = {
        "execution_id": execution_id,
        "file_name": file_name,
        "raw_text": "",
        "summary": "",
        "classified_requirements": "",
        "gap_analysis": "",
        "brd_document": "",
        "functional_specifications": "",
        "user_stories": "",
    }

    result = await graph.ainvoke(state)

    for key, filename in ARTIFACT_FILES.items():
        content = result.get(key)
        if content:
            message = await writer.write(filename, content)
            logger.info(message)

    logger.info("Pipeline complete. Artifacts written to 'output/'.")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="AI Requirements Analyst Agent")
    parser.add_argument(
        "--file",
        default=os.getenv("REQUIREMENTS_FILE", "Requirements.docx"),
        help="Name of the requirement document in the input/ directory",
    )
    args = parser.parse_args()
    asyncio.run(main(args.file))
