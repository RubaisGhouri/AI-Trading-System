"""
QuantNova Fair Value Gap Detection Engine
Uses Shared MarketDataService
"""

from app.services.market_data_service import MarketDataService


class FVGService:

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

        bullish = []
        bearish = []

        for i in range(1, len(df) - 1):

            # Bullish FVG
            if df["low"][i + 1] > df["high"][i - 1]:

                bullish.append({

                    "low": round(df["high"][i - 1], 2),

                    "high": round(df["low"][i + 1], 2),

                    "size": round(
                        df["low"][i + 1] - df["high"][i - 1],
                        2
                    )

                })

            # Bearish FVG
            if df["high"][i + 1] < df["low"][i - 1]:

                bearish.append({

                    "high": round(df["low"][i - 1], 2),

                    "low": round(df["high"][i + 1], 2),

                    "size": round(
                        df["low"][i - 1] - df["high"][i + 1],
                        2
                    )

                })

        return {

            "latest_bullish_fvg":
                bullish[-1] if bullish else None,

            "latest_bearish_fvg":
                bearish[-1] if bearish else None,

            "bullish_count":
                len(bullish),

            "bearish_count":
                len(bearish)

        }