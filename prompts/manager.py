"""
Prompt Manager.
"""

from prompts.system import SYSTEM_PROMPT


class PromptManager:
    """
    Builds prompts for all AI providers.
    """

    @staticmethod
    def build(user_prompt: str) -> tuple[str, str]:
        """
        Returns:

        system_prompt,
        user_prompt
        """

        return SYSTEM_PROMPT, user_prompt