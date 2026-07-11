"""
Portfolio Service
"""


class PortfolioService:

    @classmethod
    def get_summary(cls):

        return {
            "connected": False,
            "broker": "Not Connected",
            "balance": None,
            "today_pl": None,
            "open_trades": 0,
            "risk": "--",
        }