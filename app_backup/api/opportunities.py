from fastapi import APIRouter

from app.services.opportunity_service import OpportunityService

router = APIRouter()


@router.get("/api/opportunities")
async def opportunities():

    return OpportunityService.scan()