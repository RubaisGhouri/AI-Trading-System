"""
Abstract base class for all LLM providers.
"""

from abc import ABC, abstractmethod

from llm.response import LLMResponse


class BaseLLM(ABC):
    """
    Abstract interface that every LLM provider must implement.
    """

    @property
    @abstractmethod
    def provider_name(self) -> str:
        """
        Return the provider name.
        """
        pass

    @abstractmethod
    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> LLMResponse:
        """
        Generate a response from the LLM.
        """
        pass