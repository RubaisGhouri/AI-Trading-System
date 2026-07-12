"""
QuantNova Institutional Signal Engine v2
"""

from app.services.confluence_service import ConfluenceService


class SignalService:

    @classmethod
    def analyze(cls):

        analysis = ConfluenceService.analyze()

        tech = analysis["technical"]

        score = analysis["score"]

        signal = analysis["signal"]

        reasons = analysis["reasons"]

        price = tech["price"]

        # ===========================
        # Direction
        # ===========================

        if signal in ["BUY", "STRONG BUY"]:

            direction = "LONG"

        elif signal in ["SELL", "STRONG SELL"]:

            direction = "SHORT"

        else:

            direction = "WAIT"

        # ===========================
        # Confidence
        # ===========================

        confidence = min(abs(score), 99)

        # ===========================
        # Entry Zone
        # ===========================

        atr = tech["atr"]

        entry_low = round(price - (atr * 0.15), 2)

        entry_high = round(price + (atr * 0.15), 2)

        # ===========================
        # LONG
        # ===========================

        if direction == "LONG":

            stop_loss = round(price - atr, 2)

            tp1 = round(price + atr, 2)

            tp2 = round(price + (atr * 2), 2)

            tp3 = round(price + (atr * 3), 2)

            rr = "1 : 3"

        # ===========================
        # SHORT
        # ===========================

        elif direction == "SHORT":

            stop_loss = round(price + atr, 2)

            tp1 = round(price - atr, 2)

            tp2 = round(price - (atr * 2), 2)

            tp3 = round(price - (atr * 3), 2)

            rr = "1 : 3"

        # ===========================
        # WAIT
        # ===========================

        else:

            stop_loss = "-"

            tp1 = "-"

            tp2 = "-"

            tp3 = "-"

            rr = "-"

        return {

            "coin": "BTC/USDT",

            "signal": signal,

            "direction": direction,

            "confidence": confidence,

            "entry": f"{entry_low} - {entry_high}",

            "stop_loss": stop_loss,

            "tp1": tp1,

            "tp2": tp2,

            "tp3": tp3,

            "risk_reward": rr,

            "timeframe": "1H",

            "leverage": "3x",

            "reason": reasons,

            "score": score,

            "technical": tech,

            "institutional": {

                "smc": analysis["smc"],

                "order_blocks": analysis["order_blocks"],

                "fvg": analysis["fvg"],

                "support_resistance": analysis["support_resistance"],

                "multi_timeframe": analysis["multi_timeframe"]

            }

        }