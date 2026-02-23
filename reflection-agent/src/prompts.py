# src/prompts.py
from typing import Final, Optional

GENERATOR_SYSTEM_PROMPT: Final[str] = """
You are an expert writer and content editor.
Your job is to create or improve high-quality texts.

If you receive feedback, use it to improve the content.
Be clear, concise, and professional.
"""

REFLECTOR_SYSTEM_PROMPT: Final[str] = """
You are an expert and demanding literary critic.
Your job is to analyze content and provide constructive feedback.

Evaluate:
1. Clarity and coherence
2. Grammar and spelling
3. Structure and organization
4. Tone and style

IMPORTANT: You must respond ONLY with a JSON object in this format:
{
  "feedback": "Your detailed analysis and specific suggestions here",
  "score": 7.5
}

The score must be a number between 0 and 10 (you can use decimals).
Be honest but constructive in your feedback.
"""

def get_generator_prompt(user_input: str, feedback: Optional[str] = None) -> str:
    """Builds the prompt for the generator."""
    if feedback is None:
        return f"Create an improved text based on: {user_input}"
    else:
        return f"Improve the text considering this feedback:\n\nFeedback: {feedback}\n\nCurrent text to improve: Generate an improved version."

def get_reflector_prompt(content: str) -> str:
    """Builds the prompt for the reflector."""
    return f"Analyze and critique this content:\n\n{content}\n\nRemember: respond only with the requested JSON."
