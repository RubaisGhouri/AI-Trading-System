"""
Exchange Manager.
"""

from config.settings import settings
from exchange.binance import BinanceExchange


class ExchangeManager:
    """
    Creates and manages exchange integrations.
    """

    def __init__(self):

        exchange = settings.exchange_name.lower()

        if exchange == "binance":
            self.exchange = BinanceExchange()

        else:
            raise ValueError(
                f"Unsupported exchange: {exchange}"
            )

    def get_market_snapshot(
        self,
        symbol: str,
        timeframe: str,
    ) -> dict:

        return self.exchange.get_market_snapshot(
            symbol=symbol,
            timeframe=timeframe,
        )