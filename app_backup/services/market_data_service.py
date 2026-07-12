"""
QuantNova Shared Market Data Service
Single Binance Request + Cached DataFrame
"""

import requests
import pandas as pd

from app.services.cache_service import CacheService


class MarketDataService:

    BASE_URL = "https://api.binance.com/api/v3/klines"

    @classmethod
    def get_dataframe(

        cls,

        symbol="BTCUSDT",

        interval="1h",

        limit=300,

    ):

        cache_key = f"market_df_{symbol}_{interval}"

        cached = CacheService.get(cache_key)

        if cached is not None:

            return cached

        response = requests.get(

            cls.BASE_URL,

            params={

                "symbol": symbol,

                "interval": interval,

                "limit": limit,

            },

            timeout=5,

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

        numeric_columns = [

            "open",

            "high",

            "low",

            "close",

            "volume"

        ]

        for column in numeric_columns:

            df[column] = df[column].astype(float)

        CacheService.set(

            cache_key,

            df,

            ttl=15,

        )

        return df