"""
Binance Exchange.

Placeholder implementation.
"""

from exchange.base import BaseExchange


class BinanceExchange(BaseExchange):

    @property
    def exchange_name(self) -> str:
        return "binance"

    def get_market_snapshot(
        self,
        symbol: str,
        timeframe: str,
    ) -> dict:

        return {
            "exchange": self.exchange_name,
            "symbol": symbol,
            "timeframe": timeframe,
            "price": None,
            "volume": None,
            "trend": "unknown",
            "candles": [],
        }