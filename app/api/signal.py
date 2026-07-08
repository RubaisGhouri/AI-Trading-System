from fastapi import APIRouter

from app.services.signal_service import SignalService

router = APIRouter()


@router.get("/api/signal")
async def signal():

    return SignalService.analyze()