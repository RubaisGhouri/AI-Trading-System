"""
QuantNova Opportunity Scanner
"""

from app.services.market_analyzer import MarketAnalyzer


class OpportunityService:

    @classmethod
    def scan(cls):

        coins = MarketAnalyzer.analyze_all()

        results = []

        for coin in coins:

            score = 50

            if coin["ema20"] > coin["ema50"]:
                score += 20
            else:
                score -= 20

            if coin["rsi"] < 35:
                score += 15

            elif coin["rsi"] > 70:
                score -= 15

            score = max(0, min(score, 100))

            if score >= 80:
                signal = "BUY"

            elif score <= 40:
                signal = "SELL"

            else:
                signal = "HOLD"

            results.append({

                "coin": coin["coin"],

                "price": coin["price"],

                "signal": signal,

                "confidence": score,

                "rsi": coin["rsi"]

            })

        results.sort(

            key=lambda x: x["confidence"],

            reverse=True

        )

        return results