from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chat_service import ChatService

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/chat")
async def chat(request: ChatRequest):

    reply = ChatService.ask(request.message)

    return {
        "reply": reply
    }