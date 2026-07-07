"""
Ollama LLM Provider.
"""

from ollama import Client

from config.settings import settings
from llm.base import BaseLLM
from llm.response import LLMResponse


class OllamaLLM(BaseLLM):
    """
    Ollama implementation using local models.
    """

    def __init__(self):
        self.client = Client(host="http://localhost:11434")
        self.model = "qwen2.5:3b"

    @property
    def provider_name(self) -> str:
        return "ollama"

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> LLMResponse:

        messages = []

        if system_prompt:
            messages.append(
                {
                    "role": "system",
                    "content": system_prompt,
                }
            )

        messages.append(
            {
                "role": "user",
                "content": prompt,
            }
        )

        response = self.client.chat(
            model=self.model,
            messages=messages,
        )

        text = response["message"]["content"]

        return LLMResponse(
            text=text,
            provider=self.provider_name,
            model=self.model,
            raw_response=response,
        )