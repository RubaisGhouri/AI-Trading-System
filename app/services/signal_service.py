"""
QuantNova Institutional Signal Engine
"""

from app.services.multi_timeframe_service import MultiTimeframeService
from app.services.support_resistance_service import SupportResistanceService


class SignalService:

    @classmethod
    def analyze(cls):

        mtf = MultiTimeframeService.analyze()

        sr = SupportResistanceService.analyze()

        overall = mtf["overall"]

        tech = mtf["1h"]["technical"]

        signal = overall["signal"]

        direction = overall["direction"]

        confidence = overall["confidence"]

        price = tech["price"]

        atr = tech["atr"]

        reasons = []

        # ==================================
        # Timeframe Confirmation
        # ==================================

        if mtf["15m"]["signal"] == signal:
            reasons.append("15m confirms trend")

        if mtf["1h"]["signal"] == signal:
            reasons.append("1H confirms trend")

        if mtf["4h"]["signal"] == signal:
            reasons.append("4H confirms trend")

        # ==================================
        # Trend
        # ==================================

        reasons.append(f"Trend: {tech['trend']}")

        if tech["macd_cross"]:
            reasons.append("Bullish MACD")
        else:
            reasons.append("Bearish MACD")

        if tech["volume_breakout"]:
            reasons.append("Volume Breakout")

        if tech["adx"] > 25:
            reasons.append("Strong ADX")

        if tech["rsi"] < 30:
            reasons.append("RSI Oversold")

        elif tech["rsi"] > 70:
            reasons.append("RSI Overbought")

        else:
            reasons.append("Healthy RSI")

        # ==================================
        # Support Resistance Filter
        # ==================================

        if direction == "LONG":

            if sr["distance_to_resistance"] < 1.0:

                signal = "HOLD"

                direction = "WAIT"

                reasons.append(
                    "Resistance too close"
                )

        elif direction == "SHORT":

            if sr["distance_to_support"] < 1.0:

                signal = "HOLD"

                direction = "WAIT"

                reasons.append(
                    "Support too close"
                )

        # ==================================
        # Entry
        # ==================================

        entry_low = round(price - atr * 0.20, 2)

        entry_high = round(price + atr * 0.20, 2)

        # ==================================
        # TP SL
        # ==================================

        if direction == "LONG":

            stop_loss = round(price - (1.5 * atr), 2)

            tp1 = round(price + (1.5 * atr), 2)

            tp2 = round(price + (3 * atr), 2)

            tp3 = round(price + (5 * atr), 2)

        elif direction == "SHORT":

            stop_loss = round(price + (1.5 * atr), 2)

            tp1 = round(price - (1.5 * atr), 2)

            tp2 = round(price - (3 * atr), 2)

            tp3 = round(price - (5 * atr), 2)

        else:

            stop_loss = "-"

            tp1 = "-"

            tp2 = "-"

            tp3 = "-"

        return {

            "coin": "BTC/USDT",

            "signal": signal,

            "direction": direction,

            "confidence": confidence,

            "entry": f"{entry_low} - {entry_high}",

            "tp1": tp1,

            "tp2": tp2,

            "tp3": tp3,

            "stop_loss": stop_loss,

            "risk_reward": "1 : 2.8",

            "timeframe": "15m + 1H + 4H",

            "leverage": "3x",

            "bullish_timeframes": overall["bullish_timeframes"],

            "bearish_timeframes": overall["bearish_timeframes"],

            "support": sr["support"],

            "resistance": sr["resistance"],

            "distance_to_support": sr["distance_to_support"],

            "distance_to_resistance": sr["distance_to_resistance"],

            "reason": reasons,

            "technical": tech

        }