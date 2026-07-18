from pydantic import BaseModel
from typing import Any


class AnalysisRequest(BaseModel):
    file_name: str


class AnalysisResponse(BaseModel):
    file_name: str
    raw_text: str
    summary: Any
    classified_requirements: Any
    gap_analysis: Any
    brd_document: str
    functional_specifications: str
    user_stories: Any
