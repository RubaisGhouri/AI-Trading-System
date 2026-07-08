"""
Market API.
"""

from fastapi import APIRouter

from app.services.market_service import MarketService

router = APIRouter(
    prefix="/api/market",
    tags=["Market"],
)


@router.get("/")
def get_market():

    return MarketService.get_market_data()