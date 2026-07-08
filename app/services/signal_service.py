"""
QuantNova Signal Engine
"""

from app.services.technical_service import TechnicalService


class SignalService:

    @classmethod
    def analyze(cls):

        tech = TechnicalService.analyze()

        price = tech["price"]
        rsi = tech["rsi"]
        ema20 = tech["ema20"]
        ema50 = tech["ema50"]

        signal = "HOLD"
        confidence = 60

        # Strong Buy
        if rsi < 30 and price > ema20:
            signal = "BUY"
            confidence = 90

        # Buy
        elif price > ema20 > ema50:
            signal = "BUY"
            confidence = 82

        # Strong Sell
        elif rsi > 70 and price < ema20:
            signal = "SELL"
            confidence = 92

        # Sell
        elif price < ema20 < ema50:
            signal = "SELL"
            confidence = 82

        entry = round(price, 2)
        stop_loss = round(price * 0.985, 2)
        take_profit = round(price * 1.03, 2)

        return {
            "signal": signal,
            "confidence": confidence,
            "entry": entry,
            "stop_loss": stop_loss,
            "take_profit": take_profit,
            "technical": tech,
        }