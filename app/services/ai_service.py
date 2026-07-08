"""
QuantNova AI Service.
Handles communication with Ollama.
"""

from ollama import chat

from app.services.analysis_service import AnalysisService
from app.services.prompt_builder import PromptBuilder


class AIService:

    MODEL = "qwen2.5:3b"

    SYSTEM_PROMPT = """
You are QuantNova AI.

Developed by Rubais Ghouri.
Powered by DevSpark Creations.

You are a professional AI Trading Intelligence Assistant.

Your expertise includes:

- Cryptocurrency
- Technical Analysis
- Market Structure
- Risk Management
- Trading Psychology

Never invent market data.
Always use the supplied market context.
Base your answer on the provided context.
Keep answers professional, short and actionable.
"""

    @classmethod
    def ask(cls, message: str):

        # Get Live Market Context
        context = AnalysisService.get_context()

        # Build Prompt
        user_prompt = PromptBuilder.build(
            context=context,
            user_message=message,
        )

        # Ask Ollama
        response = chat(
            model=cls.MODEL,
            messages=[
                {
                    "role": "system",
                    "content": cls.SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": user_prompt,
                },
            ],
            options={
                "temperature": 0.2,
                "num_predict": 120,
            },
        )

        return response["message"]["content"]