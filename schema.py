from pydantic import BaseModel, Field
from typing import List

class DailyExtraction(BaseModel):
    """The structured format for our daily logs."""
    learning_topics: List[str] = Field(description="List of technical concepts learned")
    coding_work: List[str] = Field(description="List of tasks, bugs, or features completed")
    linkedin_post: str = Field(description="A professional, engaging LinkedIn post with emojis")
    github_update: str = Field(description="A concise technical summary for GitHub/Commits")
