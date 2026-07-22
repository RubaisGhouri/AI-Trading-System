"""
QuantNova AI Service.
Handles communication with Ollama.
"""

import time
from ollama import chat

from app.services.analysis_service import AnalysisService
from app.services.prompt_builder import PromptBuilder


class AIService:

    MODEL = "qwen2.5:3b"

    SYSTEM_PROMPT = """
You are QuantNova AI.

Developed by Rubais Ghouri.
Powered by DevSpark Creations.

You are a premium AI Trading Assistant.

Your personality:

- Friendly
- Professional
- Conversational
- Helpful

You specialize in:

• Cryptocurrency
• Technical Analysis
• Smart Money Concepts
• Risk Management
• Trading Psychology

Rules:

- Reply naturally.
- Never sound robotic.
- Use the provided market context only when relevant.
- If the user greets you, greet back.
- If the user asks educational questions, teach them.
- If the user asks about signals, explain the current signal.
- Never invent prices.
- Keep replies between 40 and 120 words.
"""

    @classmethod
    def ask(cls, message: str):

        print("=" * 70)
        print("QuantNova AI Request")
        print("=" * 70)

        start = time.time()

        context = AnalysisService.get_context()

        print("Context Loaded")

        prompt = PromptBuilder.build(
            context=context,
            user_message=message
        )

        print("Prompt Built Successfully")

        response = chat(
            model=cls.MODEL,
            messages=[
                {
                    "role": "system",
                    "content": cls.SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            options={
                "temperature": 0.1,
                "top_p": 0.8,
                "num_predict": 60,
                "repeat_penalty": 1.1
            }
        )

        end = time.time()

        print(f"Ollama Response Received ({round(end-start,2)} sec)")

        return response["message"]["content"].strip()