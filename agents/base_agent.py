"""
Base Agent for all AI agents.
"""

from abc import ABC

from llm.factory import LLMFactory
from llm.response import LLMResponse


class BaseAgent(ABC):
    """
    Parent class for all AI agents.
    """

    def __init__(self):
        self.llm = LLMFactory.create()

    @property
    def agent_name(self) -> str:
        return self.__class__.__name__

    def ask(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> LLMResponse:
        """
        Send prompt to the configured LLM.
        """

        return self.llm.generate(
            prompt=prompt,
            system_prompt=system_prompt,
        )