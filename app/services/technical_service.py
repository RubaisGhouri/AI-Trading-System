"""
Technical Analysis Service
"""

import requests
import pandas as pd

from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator

from app.services.cache_service import CacheService


class TechnicalService:

    BASE_URL = "https://api.binance.com/api/v3/klines"

    @classmethod
    def analyze(cls, symbol="BTCUSDT", interval="1h", limit=200):

        cache_key = f"technical_{symbol}_{interval}"

        cached = CacheService.get(cache_key)

        if cached:
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
            ],
        )

        df["close"] = df["close"].astype(float)

        rsi = RSIIndicator(df["close"], window=14)
        ema20 = EMAIndicator(df["close"], window=20)
        ema50 = EMAIndicator(df["close"], window=50)

        result = {
            "price": round(float(df["close"].iloc[-1]), 2),
            "rsi": round(float(rsi.rsi().iloc[-1]), 2),
            "ema20": round(float(ema20.ema_indicator().iloc[-1]), 2),
            "ema50": round(float(ema50.ema_indicator().iloc[-1]), 2),
        }

        CacheService.set(cache_key, result, ttl=15)

        return result