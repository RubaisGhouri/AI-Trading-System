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

            results.append({

                "coin": coin["coin"],

                "price": coin["price"],

                "signal": coin["signal"],

                "direction": coin["direction"],

                "confidence": coin["confidence"],

                "trend": coin["trend"]

            })

        results.sort(

            key=lambda x: x["confidence"],

            reverse=True

        )

        return results