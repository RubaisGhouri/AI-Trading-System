"""
Ollama LLM Provider.
"""

from ollama import Client

from llm.base import BaseLLM
from llm.response import LLMResponse
from prompts.manager import PromptManager


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
        """
        Generate a response using Ollama.
        """

        # Build prompts using the Prompt Manager
        default_system_prompt, user_prompt = PromptManager.build(prompt)

        # If caller provides a custom system prompt,
        # use it instead of the default QuantNova prompt.
        final_system_prompt = system_prompt or default_system_prompt

        messages = [
            {
                "role": "system",
                "content": final_system_prompt,
            },
            {
                "role": "user",
                "content": user_prompt,
            },
        ]

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