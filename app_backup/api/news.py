"""
News API
"""

from fastapi import APIRouter
from app.services.news_service import NewsService

router = APIRouter()


@router.get("/api/news")
def get_news():
    return NewsService.get_news()