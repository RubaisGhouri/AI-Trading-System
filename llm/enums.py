"""
Enumerations used by the LLM module.
"""

from enum import Enum


class LLMProvider(str, Enum):
    """
    Supported LLM providers.
    """

    GEMINI = "gemini"
    CLAUDE = "claude"
    OPENAI = "openai"
    DEEPSEEK = "deepseek"
    OLLAMA = "ollama"


class LLMRole(str, Enum):
    """
    Standard message roles.
    """

    SYSTEM = "system"
    USER = "user"
    ASSISTANT = "assistant"