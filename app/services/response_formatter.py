"""
Response Formatter
"""


class ResponseFormatter:

    @staticmethod
    def clean(text: str) -> str:

        if not text:
            return "I'm sorry, I couldn't generate a response."

        text = text.replace("**", "")

        text = text.replace("###", "")

        text = text.strip()

        return text