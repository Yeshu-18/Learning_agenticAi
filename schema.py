from pydantic import BaseModel, Field
from typing import List

class DailyExtraction(BaseModel):
    """The structured format for our daily dev logs."""
    learning_topics: List[str] = Field(description="Key technical concepts or tools learned today")
    coding_work: List[str] = Field(description="Specific tasks, bug fixes, or features shipped")
    linkedin_post: str = Field(description="A viral-worthy LinkedIn post with hook, story, value, and CTA")
