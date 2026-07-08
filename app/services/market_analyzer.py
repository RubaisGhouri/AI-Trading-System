"""
QuantNova Multi Coin Analyzer
"""

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

    @classmethod
    def analyze_all(cls):

        markets = []

        for coin in cls.COINS:

            tech = TechnicalService.analyze(symbol=coin)

            markets.append({

                "coin": coin.replace("USDT", ""),

                **tech

            })

        return markets