import ollama
import json
import re
from schema import DailyExtraction

class ExtractionEngine:
    def __init__(self, model_name="gemma4:e4b"):
        self.model_name = model_name

    def process_notes(self, raw_notes: str) -> DailyExtraction:
        prompt = f"""You are a developer's personal content strategist.
Parse the raw notes below into structured JSON.

EXTRACTION RULES:
- "learning_topics": Short, specific technical concepts (e.g., "WebSockets", "Docker multi-stage builds"). No filler.
- "coding_work": One-line descriptions of tasks shipped (e.g., "Built a REST API for user auth with JWT"). Be specific.
- "linkedin_post": A scroll-stopping LinkedIn post following this structure:
    1. HOOK (1-2 lines): A bold, curiosity-driven opener. Use a hot take, a surprising stat, or a relatable pain point. Start with an emoji.
    2. STORY (3-5 lines): What you did today in a narrative style. Be specific—mention tools, frameworks, and real challenges.
    3. KEY TAKEAWAY (1-2 lines): A concise, quotable insight others can learn from.
    4. CTA (1-2 lines): End with a question or call to engage. Use a relevant emoji.
    FORMAT: Use line breaks between sections for readability. Keep it under 200 words. Use 3-5 emojis total (not excessive). Avoid hashtag spam—use at most 3 relevant hashtags at the end.

RAW NOTES:
{raw_notes}

Return ONLY valid JSON:
{{
  "learning_topics": [],
  "coding_work": [],
  "linkedin_post": ""
}}"""

        response = ollama.generate(model=self.model_name, prompt=prompt)
        raw_output = response['response']

        # Clean the output: Remove markdown code blocks if present
        clean_json = re.sub(r'```json|```', '', raw_output).strip()

        try:
            data_dict = json.loads(clean_json)
            return DailyExtraction(**data_dict)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON. Error: {e}. Raw output: {raw_output}")
