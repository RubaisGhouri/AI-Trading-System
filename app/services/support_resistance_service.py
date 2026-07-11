"""
QuantNova Support & Resistance Engine
"""

import requests
import pandas as pd


class SupportResistanceService:

    BASE_URL = "https://api.binance.com/api/v3/klines"

    @classmethod
    def analyze(
        cls,
        symbol="BTCUSDT",
        interval="1h",
        limit=200
    ):

        response = requests.get(

            cls.BASE_URL,

            params={
                "symbol": symbol,
                "interval": interval,
                "limit": limit,
            },

            timeout=5

        )

        candles = response.json()

        df = pd.DataFrame(

            candles,

            columns=[

                "open_time",

                "open",

                "high",

                "low",

                "close",

                "volume",

                "close_time",

                "quote_asset_volume",

                "trades",

                "tb_base",

                "tb_quote",

                "ignore",

            ]

        )

        df["high"] = df["high"].astype(float)

        df["low"] = df["low"].astype(float)

        df["close"] = df["close"].astype(float)

        current_price = float(df["close"].iloc[-1])

        resistance = round(df["high"].tail(50).max(), 2)

        support = round(df["low"].tail(50).min(), 2)

        resistance_distance = round(

            ((resistance-current_price)/current_price)*100,

            2

        )

        support_distance = round(

            ((current_price-support)/current_price)*100,

            2

        )

        return {

            "price": round(current_price,2),

            "support": support,

            "resistance": resistance,

            "distance_to_support": support_distance,

            "distance_to_resistance": resistance_distance

        }