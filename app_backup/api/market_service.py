"""
Market Data Service
QuantNova

Developed by Rubais Ghouri
Powered by DevSpark Creations
"""

import requests


class MarketService:

    BASE_URL = "https://api.binance.com/api/v3/ticker/24hr"

    SYMBOLS = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
        "XRPUSDT",
        "DOGEUSDT",
        "ADAUSDT",
    ]

    @classmethod
    def get_market_data(cls):

        markets = []

        for symbol in cls.SYMBOLS:

            try:

                response = requests.get(
                    cls.BASE_URL,
                    params={"symbol": symbol},
                    timeout=5,
                )

                response.raise_for_status()

                data = response.json()

                markets.append(
                    {
                        "symbol": symbol.replace("USDT", ""),
                        "price": round(float(data["lastPrice"]), 2),
                        "change": round(float(data["priceChangePercent"]), 2),
                        "volume": round(float(data["volume"]), 2),
                        "high": round(float(data["highPrice"]), 2),
                        "low": round(float(data["lowPrice"]), 2),
                    }
                )

            except Exception:

                markets.append(
                    {
                        "symbol": symbol.replace("USDT", ""),
                        "price": 0,
                        "change": 0,
                        "volume": 0,
                        "high": 0,
                        "low": 0,
                    }
                )

        return markets