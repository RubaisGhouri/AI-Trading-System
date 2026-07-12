"""
Market Data Service.

Fetches live market data from Binance.
"""

import requests


class MarketService:
    """
    Binance Market Service.
    """

    BASE_URL = "https://api.binance.com/api/v3/ticker/24hr"

    SYMBOLS = [
        "BTCUSDT",
        "ETHUSDT",
        "BNBUSDT",
        "SOLUSDT",
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

                data = response.json()

                markets.append(
                    {
                        "symbol": symbol.replace("USDT", ""),
                        "price": float(data["lastPrice"]),
                        "change": float(data["priceChangePercent"]),
                        "volume": float(data["volume"]),
                    }
                )

            except Exception:

                markets.append(
                    {
                        "symbol": symbol.replace("USDT", ""),
                        "price": 0,
                        "change": 0,
                        "volume": 0,
                    }
                )

        return markets