"""
Application configuration using Pydantic Settings.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application settings.
    Values are loaded automatically from the .env file.
    """

    # -------------------------------------------------
    # Environment
    # -------------------------------------------------

    environment: str = "development"
    debug: bool = True

    # -------------------------------------------------
    # Application
    # -------------------------------------------------

    app_name: str = "QuantNova"
    app_version: str = "1.0.0"

    # -------------------------------------------------
    # Branding
    # -------------------------------------------------

    ai_name: str = "QuantNova"
    ai_tagline: str = "Advanced AI Trading Intelligence Platform"
    ai_developer: str = "Rubais Ghouri"
    ai_company: str = "DevSpark Creations"

    # -------------------------------------------------
    # AI Providers
    # -------------------------------------------------

    default_llm: str = "ollama"

    gemini_api_key: str = ""
    openai_api_key: str = ""
    claude_api_key: str = ""
    deepseek_api_key: str = ""

    # -------------------------------------------------
    # Exchange
    # -------------------------------------------------

    exchange_name: str = "binance"

    binance_api_key: str = ""
    binance_secret_key: str = ""

    # -------------------------------------------------
    # Logging
    # -------------------------------------------------

    log_level: str = "INFO"

    # -------------------------------------------------
    # Pydantic Configuration
    # -------------------------------------------------

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )


settings = Settings()