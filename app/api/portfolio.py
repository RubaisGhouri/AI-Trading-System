from fastapi import APIRouter

from app.services.portfolio_service import PortfolioService

router = APIRouter()


@router.get("/portfolio")
def portfolio():

    return PortfolioService.get_summary()