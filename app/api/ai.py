from fastapi import APIRouter
from pydantic import BaseModel

from app.services.ai_service import AIService

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    reply = AIService.ask(request.message)

    return {
        "reply": reply
    }