"""
Central logger.
"""

import logging
from pathlib import Path

from config.settings import settings
from core.logging_config import (
    LOG_FORMAT,
    DATE_FORMAT,
)

LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)

LOG_FILE = LOG_DIR / "quantnova.log"

logger = logging.getLogger(settings.app_name)

logger.setLevel(getattr(logging, settings.log_level))

formatter = logging.Formatter(
    LOG_FORMAT,
    datefmt=DATE_FORMAT,
)

file_handler = logging.FileHandler(
    LOG_FILE,
    encoding="utf-8",
)

file_handler.setFormatter(formatter)

console_handler = logging.StreamHandler()

console_handler.setFormatter(formatter)

logger.handlers.clear()

logger.addHandler(file_handler)

logger.addHandler(console_handler)

logger.propagate = False