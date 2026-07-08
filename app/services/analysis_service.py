"""
Analysis Service
"""

from app.services.market_service import MarketService
from app.services.signal_service import SignalService
from app.services.cache_service import CacheService


class AnalysisService:

    @classmethod
    def get_context(cls):

        cached = CacheService.get("analysis")

        if cached:
            return cached

        context = {
            "market": MarketService.get_market_data(),
            "analysis": SignalService.analyze(),
        }

        CacheService.set(
            "analysis",
            context,
            ttl=15,
        )

        return context