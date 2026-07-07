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

    app_name: str = "AI Trading System"
    app_version: str = "1.0.0"

    # -------------------------------------------------
    # AI Providers
    # -------------------------------------------------

    default_llm: str = "gemini"

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