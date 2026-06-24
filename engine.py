import ollama
import json
import re
from schema import DailyExtraction

class ExtractionEngine:
    def __init__(self, model_name="gemma4:e4b"):
        self.model_name = model_name

    def process_notes(self, raw_notes: str) -> DailyExtraction:
        prompt = f"""
        You are a professional content extractor. 
        Task: Parse the following raw notes into a structured JSON format.
        
        Rules:
        1. 'learning_topics': Extract only core technical concepts.
        2. 'coding_work': Extract specific tasks, bug fixes, or features.
        3. 'linkedin_post': Write a professional, engaging post using the 'Hook -> Value -> CTA' framework. Use emojis.
        4. 'github_update': Write a concise, technical summary for a commit message or README.

        Notes to process:
        {raw_notes}

        Return ONLY valid JSON that matches this schema:
        {{
          "learning_topics": [],
          "coding_work": [],
          "linkedin_post": "",
          "github_update": ""
        }}
        """

        response = ollama.generate(model=self.model_name, prompt=prompt)
        raw_output = response['response']

        # Clean the output: Remove markdown code blocks if present
        clean_json = re.sub(r'```json|```', '', raw_output).strip()

        try:
            data_dict = json.loads(clean_json)
            return DailyExtraction(**data_dict)
        except Exception as e:
            raise ValueError(f"Failed to parse JSON. Error: {e}. Raw output: {raw_output}")
