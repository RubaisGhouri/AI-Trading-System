"""
QuantNova Multi Timeframe Analysis Engine
"""

from app.services.technical_service import TechnicalService


class MultiTimeframeService:

    TIMEFRAMES = [

        "15m",

        "1h",

        "4h",

    ]

    @classmethod
    def analyze(cls, symbol="BTCUSDT"):

        analysis = {}

        total_score = 0

        bullish = 0

        bearish = 0

        for timeframe in cls.TIMEFRAMES:

            tech = TechnicalService.analyze(

                symbol=symbol,

                interval=timeframe

            )

            score = 50

            # ==========================
            # EMA Trend
            # ==========================

            if tech["trend"] == "BULLISH":

                score += 20

            elif tech["trend"] == "BEARISH":

                score -= 20

            # ==========================
            # RSI
            # ==========================

            if tech["rsi"] < 30:

                score += 15

            elif tech["rsi"] > 70:

                score -= 15

            # ==========================
            # MACD
            # ==========================

            if tech["macd_cross"]:

                score += 15

            else:

                score -= 15

            # ==========================
            # ADX
            # ==========================

            if tech["adx"] > 25:

                score += 10

            # ==========================
            # Volume
            # ==========================

            if tech["volume_breakout"]:

                score += 10

            score = max(0, min(score, 100))

            if score >= 70:

                signal = "BUY"

                bullish += 1

            elif score <= 30:

                signal = "SELL"

                bearish += 1

            else:

                signal = "HOLD"

            analysis[timeframe] = {

                "signal": signal,

                "score": score,

                "technical": tech

            }

            total_score += score

        average_score = round(

            total_score / len(cls.TIMEFRAMES),

            2

        )

        # ==========================
        # Overall Decision
        # ==========================

        if bullish >= 2:

            overall_signal = "BUY"

            direction = "LONG"

        elif bearish >= 2:

            overall_signal = "SELL"

            direction = "SHORT"

        else:

            overall_signal = "HOLD"

            direction = "WAIT"

        analysis["overall"] = {

            "signal": overall_signal,

            "direction": direction,

            "confidence": average_score,

            "bullish_timeframes": bullish,

            "bearish_timeframes": bearish

        }

        return analysis