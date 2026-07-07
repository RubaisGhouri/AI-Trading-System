"""
Custom exceptions for the AI Trading System.

Instead of raising generic exceptions, use these
custom exceptions throughout the project.
"""


class TradingSystemError(Exception):
    """
    Base exception for the AI Trading System.
    All custom exceptions should inherit from this class.
    """
    pass


class ConfigurationError(TradingSystemError):
    """Raised when configuration is invalid."""
    pass


class LLMError(TradingSystemError):
    """Raised when an LLM provider fails."""
    pass


class ExchangeError(TradingSystemError):
    """Raised when exchange operations fail."""
    pass


class StrategyError(TradingSystemError):
    """Raised when a trading strategy fails."""
    pass


class DataError(TradingSystemError):
    """Raised when market data is invalid or unavailable."""
    pass


class APIError(TradingSystemError):
    """Raised when an external API request fails."""
    pass