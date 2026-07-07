"""
Google Gemini LLM Provider.
"""

from google import genai

from config.settings import settings
from llm.base import BaseLLM
from llm.response import LLMResponse


class GeminiLLM(BaseLLM):
    """
    Google Gemini implementation.
    """

    MODEL_NAME = "gemini-2.5-flash"

    def __init__(self) -> None:
        """
        Lazy initialization.
        Client tab banega jab pehli request bheji jayegi.
        """
        self._client = None

    @property
    def provider_name(self) -> str:
        return "gemini"

    def _get_client(self):
        """
        Create the Gemini client only when needed.
        """

        if self._client is None:

            if not settings.gemini_api_key:
                raise ValueError(
                    "GEMINI_API_KEY is missing. Please add it to your .env file."
                )

            self._client = genai.Client(
                api_key=settings.gemini_api_key
            )

        return self._client

    def generate(
        self,
        prompt: str,
        system_prompt: str | None = None,
    ) -> LLMResponse:
        """
        Generate a response using Gemini.
        """

        try:

            final_prompt = prompt

            if system_prompt:
                final_prompt = f"{system_prompt}\n\n{prompt}"

            client = self._get_client()

            response = client.models.generate_content(
                model=self.MODEL_NAME,
                contents=final_prompt,
            )

            return LLMResponse(
                text=response.text,
                provider=self.provider_name,
                model=self.MODEL_NAME,
            )

        except Exception as e:
            raise RuntimeError(
                f"Gemini request failed: {e}"
            ) from e