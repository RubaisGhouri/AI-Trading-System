"""
QuantNova Order Block Detection Engine
Uses Shared MarketDataService
"""

from app.services.market_data_service import MarketDataService


class OrderBlockService:

    @classmethod
    def analyze(
        cls,
        symbol="BTCUSDT",
        interval="1h",
        limit=300,
    ):

        df = MarketDataService.get_dataframe(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        bullish_ob = None
        bearish_ob = None

        for i in range(len(df) - 2):

            # Bullish Order Block
            if (
                df["close"][i] < df["open"][i]
                and df["close"][i + 1] > df["high"][i]
            ):

                bullish_ob = {

                    "low": round(df["low"][i], 2),

                    "high": round(df["high"][i], 2),

                    "type": "BULLISH"

                }

            # Bearish Order Block
            if (
                df["close"][i] > df["open"][i]
                and df["close"][i + 1] < df["low"][i]
            ):

                bearish_ob = {

                    "low": round(df["low"][i], 2),

                    "high": round(df["high"][i], 2),

                    "type": "BEARISH"

                }

        return {

            "bullish_order_block": bullish_ob,

            "bearish_order_block": bearish_ob

        }