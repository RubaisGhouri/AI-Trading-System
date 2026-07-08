"""
QuantNova AI Service.
Handles communication with Ollama.
"""

from ollama import chat


class AIService:

    MODEL = "qwen2.5:3b"

    SYSTEM_PROMPT = """
You are QuantNova AI.

Developed by Rubais Ghouri.
Powered by DevSpark Creations.

You are an expert in:

- Cryptocurrency
- Trading
- Technical Analysis
- Risk Management
- Market Psychology

Always answer professionally.
Keep responses clear and concise.
"""

    @classmethod
    def ask(cls, message: str):

        response = chat(
            model=cls.MODEL,
            messages=[
                {
                    "role": "system",
                    "content": cls.SYSTEM_PROMPT,
                },
                {
                    "role": "user",
                    "content": message,
                },
            ],
        )

        return response["message"]["content"]