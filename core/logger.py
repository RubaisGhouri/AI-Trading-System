"""
Central logging configuration for the AI Trading System.
"""

import logging

from core.constants import LOG_FORMAT, LOG_LEVEL
from core.paths import LOGS_DIR

# Main log file
LOG_FILE = LOGS_DIR / "system.log"

# Configure logger
logging.basicConfig(
    level=getattr(logging, LOG_LEVEL),
    format=LOG_FORMAT,
    handlers=[
        logging.FileHandler(LOG_FILE, encoding="utf-8"),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger("AI-Trading-System")