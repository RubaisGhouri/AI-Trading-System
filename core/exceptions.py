"""
Custom exceptions used throughout QuantNova.
"""


class QuantNovaError(Exception):
    """
    Base exception for the application.
    """

    pass


# =====================================================
# Configuration
# =====================================================

class ConfigurationError(QuantNovaError):
    """
    Invalid or missing configuration.
    """

    pass


# =====================================================
# LLM
# =====================================================

class LLMError(QuantNovaError):
    """
    Base LLM exception.
    """

    pass


class ProviderNotAvailableError(LLMError):
    """
    Provider is unavailable.
    """

    pass


class InvalidAPIKeyError(LLMError):
    """
    Invalid API key.
    """

    pass


# =====================================================
# Exchange
# =====================================================

class ExchangeError(QuantNovaError):
    """
    Base exchange exception.
    """

    pass


class ExchangeConnectionError(ExchangeError):
    """
    Unable to connect.
    """

    pass


class InvalidSymbolError(ExchangeError):
    """
    Invalid trading symbol.
    """

    pass


class RateLimitError(ExchangeError):
    """
    API rate limit exceeded.
    """

    pass


# =====================================================
# Strategy
# =====================================================

class StrategyError(QuantNovaError):
    """
    Strategy failure.
    """

    pass


# =====================================================
# Risk
# =====================================================

class RiskManagementError(QuantNovaError):
    """
    Risk calculation failed.
    """

    pass