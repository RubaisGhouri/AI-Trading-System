"""
QuantNova Technical Analysis Engine
"""

import requests
import pandas as pd

from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator
from ta.trend import MACD
from ta.trend import ADXIndicator
from ta.volatility import AverageTrueRange

from app.services.cache_service import CacheService


class TechnicalService:

    BASE_URL = "https://api.binance.com/api/v3/klines"

    @classmethod
    def analyze(
        cls,
        symbol="BTCUSDT",
        interval="1h",
        limit=300,
    ):

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

        df["open"] = df["open"].astype(float)

        df["high"] = df["high"].astype(float)

        df["low"] = df["low"].astype(float)

        df["close"] = df["close"].astype(float)

        df["volume"] = df["volume"].astype(float)

        # ======================
        # Indicators
        # ======================

        rsi = RSIIndicator(df["close"], window=14)

        ema20 = EMAIndicator(df["close"], window=20)

        ema50 = EMAIndicator(df["close"], window=50)

        ema100 = EMAIndicator(df["close"], window=100)

        ema200 = EMAIndicator(df["close"], window=200)

        macd = MACD(df["close"])

        atr = AverageTrueRange(

            high=df["high"],

            low=df["low"],

            close=df["close"],

            window=14,

        )

        adx = ADXIndicator(

            high=df["high"],

            low=df["low"],

            close=df["close"],

            window=14,

        )

        volume_sma = df["volume"].rolling(20).mean()

                # ======================
        # Latest Values
        # ======================

        price = float(df["close"].iloc[-1])

        latest_rsi = float(rsi.rsi().iloc[-1])

        latest_ema20 = float(ema20.ema_indicator().iloc[-1])

        latest_ema50 = float(ema50.ema_indicator().iloc[-1])

        latest_ema100 = float(ema100.ema_indicator().iloc[-1])

        latest_ema200 = float(ema200.ema_indicator().iloc[-1])

        latest_macd = float(macd.macd().iloc[-1])

        latest_macd_signal = float(macd.macd_signal().iloc[-1])

        latest_adx = float(adx.adx().iloc[-1])

        latest_atr = float(atr.average_true_range().iloc[-1])

        latest_volume = float(df["volume"].iloc[-1])

        latest_volume_sma = float(volume_sma.iloc[-1])

        # ======================
        # Trend Detection
        # ======================

        if latest_ema20 > latest_ema50 > latest_ema100 > latest_ema200:

            trend = "BULLISH"

        elif latest_ema20 < latest_ema50 < latest_ema100 < latest_ema200:

            trend = "BEARISH"

        else:

            trend = "SIDEWAYS"

        # ======================
        # MACD
        # ======================

        macd_cross = latest_macd > latest_macd_signal

        # ======================
        # Volume
        # ======================

        volume_breakout = latest_volume > latest_volume_sma

        # ======================
        # Volatility
        # ======================

        volatility = round((latest_atr / price) * 100, 2)

        # ======================
        # Return
        # ======================

        result = {

            "price": round(price,2),

            "rsi": round(latest_rsi,2),

            "ema20": round(latest_ema20,2),

            "ema50": round(latest_ema50,2),

            "ema100": round(latest_ema100,2),

            "ema200": round(latest_ema200,2),

            "macd": round(latest_macd,4),

            "macd_signal": round(latest_macd_signal,4),

            "macd_cross": macd_cross,

            "adx": round(latest_adx,2),

            "atr": round(latest_atr,2),

            "trend": trend,

            "volume": round(latest_volume,2),

            "volume_sma": round(latest_volume_sma,2),

            "volume_breakout": volume_breakout,

            "volatility": volatility

        }

        CacheService.set(

            cache_key,

            result,

            ttl=15,

        )

        return result