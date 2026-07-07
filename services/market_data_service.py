"""
Market Data Service.

Provides market data to AI agents.
"""

from exchange.manager import ExchangeManager


class MarketDataService:
    """
    Service responsible for retrieving market data.
    """

    def __init__(self):
        self.exchange = ExchangeManager()

    def get_market_snapshot(
        self,
        symbol: str,
        timeframe: str,
    ) -> dict:
        """
        Returns a market snapshot.
        """

        return self.exchange.get_market_snapshot(
            symbol=symbol,
            timeframe=timeframe,
        )