"""
QuantNova Technical Analysis Engine
Uses Shared MarketDataService
"""

from ta.momentum import RSIIndicator
from ta.trend import EMAIndicator, MACD, ADXIndicator
from ta.volatility import AverageTrueRange

from app.services.cache_service import CacheService
from app.services.market_data_service import MarketDataService


class TechnicalService:

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

        # ==========================================
        # Shared DataFrame
        # ==========================================

        df = MarketDataService.get_dataframe(
            symbol=symbol,
            interval=interval,
            limit=limit,
        )

        # ==========================================
        # Indicators
        # ==========================================

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

        # ==========================================
        # Latest Values
        # ==========================================

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

        # ==========================================
        # Trend
        # ==========================================

        if latest_ema20 > latest_ema50 > latest_ema100 > latest_ema200:

            trend = "BULLISH"

        elif latest_ema20 < latest_ema50 < latest_ema100 < latest_ema200:

            trend = "BEARISH"

        else:

            trend = "SIDEWAYS"

        macd_cross = latest_macd > latest_macd_signal

        volume_breakout = latest_volume > latest_volume_sma

        volatility = round((latest_atr / price) * 100, 2)

        result = {

            "price": round(price, 2),

            "rsi": round(latest_rsi, 2),

            "ema20": round(latest_ema20, 2),

            "ema50": round(latest_ema50, 2),

            "ema100": round(latest_ema100, 2),

            "ema200": round(latest_ema200, 2),

            "macd": round(latest_macd, 4),

            "macd_signal": round(latest_macd_signal, 4),

            "macd_cross": macd_cross,

            "adx": round(latest_adx, 2),

            "atr": round(latest_atr, 2),

            "trend": trend,

            "volume": round(latest_volume, 2),

            "volume_sma": round(latest_volume_sma, 2),

            "volume_breakout": volume_breakout,

            "volatility": volatility,

        }

        CacheService.set(
            cache_key,
            result,
            ttl=15,
        )

        return result