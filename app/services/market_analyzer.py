"""
QuantNova AI Multi Coin Analyzer
"""

from concurrent.futures import ThreadPoolExecutor

from app.services.technical_service import TechnicalService


class MarketAnalyzer:

    COINS = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "ADAUSDT",
    ]

    @staticmethod
    def analyze_coin(symbol):

        tech = TechnicalService.analyze(symbol=symbol)

        signal = "HOLD"
        direction = "WAIT"
        confidence = 65

        buy_score = 0
        sell_score = 0

        if tech["trend"] == "BULLISH":
            buy_score += 1

        if tech["trend"] == "BEARISH":
            sell_score += 1

        if tech["price"] > tech["ema20"]:
            buy_score += 1
        else:
            sell_score += 1

        if tech["macd_cross"]:
            buy_score += 1
        else:
            sell_score += 1

        if tech["rsi"] < 35:
            buy_score += 1

        if tech["rsi"] > 70:
            sell_score += 1

        if tech["volume_breakout"]:
            buy_score += 1

        if buy_score >= 4:

            signal = "BUY"
            direction = "LONG"
            confidence = 90

        elif sell_score >= 4:

            signal = "SELL"
            direction = "SHORT"
            confidence = 90

        elif buy_score >= 3:

            signal = "BUY"
            direction = "LONG"
            confidence = 80

        elif sell_score >= 3:

            signal = "SELL"
            direction = "SHORT"
            confidence = 80

        return {

            "coin": symbol.replace("USDT", ""),

            "signal": signal,

            "direction": direction,

            "confidence": confidence,

            "price": tech["price"],

            "trend": tech["trend"]

        }

    @classmethod
    def analyze_all(cls):

        with ThreadPoolExecutor(max_workers=7) as executor:

            result = list(
                executor.map(
                    cls.analyze_coin,
                    cls.COINS
                )
            )

        result.sort(
            key=lambda x: x["confidence"],
            reverse=True
        )

        return result