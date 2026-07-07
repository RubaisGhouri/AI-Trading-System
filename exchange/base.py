"""
Base Exchange Interface.
"""

from abc import ABC, abstractmethod


class BaseExchange(ABC):
    """
    Base class for all exchange integrations.
    """

    @property
    @abstractmethod
    def exchange_name(self) -> str:
        """
        Exchange name.
        """
        ...

    @abstractmethod
    def get_market_snapshot(
        self,
        symbol: str,
        timeframe: str,
    ) -> dict:
        """
        Return market snapshot.
        """
        ...