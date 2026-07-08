from fastapi import APIRouter

from app.services.market_analyzer import MarketAnalyzer

router = APIRouter()


@router.get("/api/scanner")
async def scanner():

    return MarketAnalyzer.analyze_all()