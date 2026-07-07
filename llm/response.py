"""
Unified response model for all LLM providers.
"""

from dataclasses import dataclass
from typing import Any


@dataclass(slots=True)
class LLMResponse:
    """
    Standard response returned by every LLM provider.
    """

    # Main Response
    text: str
    provider: str
    model: str

    # Token Usage
    input_tokens: int = 0
    output_tokens: int = 0
    total_tokens: int = 0

    # Metadata
    finish_reason: str = "stop"
    latency_ms: float = 0.0

    # Original provider response (for debugging/logging)
    raw_response: Any | None = None