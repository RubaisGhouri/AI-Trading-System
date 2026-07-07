"""
Project paths used throughout the AI Trading System.
"""

from pathlib import Path

# Root Directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Common Directories
APP_DIR = BASE_DIR / "app"
CONFIG_DIR = BASE_DIR / "config"
CORE_DIR = BASE_DIR / "core"
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"
EXCHANGE_DIR = BASE_DIR / "exchange"
LLM_DIR = BASE_DIR / "llm"
LOGS_DIR = BASE_DIR / "logs"
SERVICES_DIR = BASE_DIR / "services"
TESTS_DIR = BASE_DIR / "tests"

# Ensure required directories exist
LOGS_DIR.mkdir(exist_ok=True)