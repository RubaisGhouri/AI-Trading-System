"""
Global constants for the AI Trading System.

This module stores project-wide constant values.
Avoid hardcoding the same values across multiple files.
"""

# ------------------------------------------------------------------
# Application Information
# ------------------------------------------------------------------

APP_NAME = "AI Trading System"
APP_VERSION = "1.0.0"
APP_ENVIRONMENT = "development"

# ------------------------------------------------------------------
# Time Settings
# ------------------------------------------------------------------

DEFAULT_TIMEZONE = "UTC"

# ------------------------------------------------------------------
# Logging
# ------------------------------------------------------------------

LOG_LEVEL = "INFO"

LOG_FORMAT = (
    "%(asctime)s | %(levelname)s | %(name)s | %(message)s"
)

# ------------------------------------------------------------------
# Supported AI Providers
# ------------------------------------------------------------------

SUPPORTED_LLMS = [
    "gemini",
    "ollama",
    "deepseek",
    "claude",
    "openai"
]