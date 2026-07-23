"""
QuantNova AI Service
Handles communication with Ollama.
"""

import time

from ollama import chat

from app.services.analysis_service import AnalysisService
from app.services.prompt_builder import PromptBuilder
from app.services.intent_service import IntentService
from app.services.local_reply_service import LocalReplyService


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

Always reply naturally like ChatGPT.

Never sound robotic.

Never repeat the same wording unnecessarily.

Be conversational, friendly and professional.

Never invent market data.

Always use the supplied market context.

Base your answer on the provided context.

Keep answers concise, actionable and easy to understand.
"""

    @classmethod
    def ask(cls, message: str):

        print("=" * 70)
        print("QuantNova AI Request")
        print("=" * 70)

        start = time.time()

        intent = IntentService.detect(message)

        print(f"Intent: {intent}")

        text = message.lower().strip()

        # ==========================================================
        # Greetings
        # ==========================================================

        if intent == "greeting":

            if "assalam" in text or "salam" in text:
                print("Greeting handled locally")
                return LocalReplyService.salam()

            elif "good morning" in text:
                print("Greeting handled locally")
                return LocalReplyService.morning()

            elif "good afternoon" in text:
                print("Greeting handled locally")
                return LocalReplyService.afternoon()

            elif "good evening" in text:
                print("Greeting handled locally")
                return LocalReplyService.evening()

            elif "hey" in text:
                print("Greeting handled locally")
                return LocalReplyService.hey()

            elif "hi" in text:
                print("Greeting handled locally")
                return LocalReplyService.hi()

            else:
                print("Greeting handled locally")
                return LocalReplyService.hello()

        # ==========================================================
        # Thanks
        # ==========================================================

        if intent == "thanks":

            print("Thanks handled locally")

            return LocalReplyService.thanks()

        # ==========================================================
        # Goodbye
        # ==========================================================

        if intent == "bye":

            print("Goodbye handled locally")

            return LocalReplyService.goodbye()

        # ==========================================================
        # AI Request
        # ==========================================================

        context = AnalysisService.get_context()

        print("Context Loaded")

        user_prompt = PromptBuilder.build(
            context=context,
            user_message=message,
        )

        print("Prompt Built Successfully")

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
                "temperature": 0.35,
                "num_predict": 100,
            },
        )

        print("Ollama Response Received")

        end = time.time()

        print(f"Completed in {round(end-start,2)} sec")

        return response["message"]["content"]