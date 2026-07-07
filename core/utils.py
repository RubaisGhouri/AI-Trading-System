"""
Common utility functions for the AI Trading System.
"""

from datetime import datetime, timezone
import uuid


def utc_now() -> datetime:
    """
    Return the current UTC datetime.
    """
    return datetime.now(timezone.utc)


def generate_id() -> str:
    """
    Generate a unique ID.
    """
    return str(uuid.uuid4())