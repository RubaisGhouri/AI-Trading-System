"""
LLM Factory.

Creates the correct LLM provider based on configuration.
"""

from config.settings import settings

from llm.providers.gemini import GeminiLLM
from llm.providers.ollama import OllamaLLM


class LLMFactory:
    """
    Factory class responsible for creating LLM providers.
    """

    @staticmethod
    def create():
        provider = settings.default_llm.lower()

        if provider == "gemini":
            return GeminiLLM()

        elif provider == "ollama":
            return OllamaLLM()

        raise ValueError(
            f"Unsupported or not yet implemented provider: {provider}"
        )