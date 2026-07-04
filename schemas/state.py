from typing import TypedDict, Optional

class RequirementState(TypedDict):
    file_name: str
    raw_text: str
    summary: dict
    classified_requirements: list
    gap_analysis: list
    brd_document: str
    functional_specifications: str
    user_stories: list