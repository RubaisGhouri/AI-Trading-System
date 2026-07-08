"""
QuantNova FastAPI Application.
"""

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.routes.home import router as home_router
from app.api.market import router as market_router
from app.api.ai import router as ai_router

app = FastAPI(
    title="QuantNova",
    description="Advanced AI Trading Intelligence Platform",
    version="1.0.0",
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

# Routes
app.include_router(home_router)
app.include_router(market_router)
app.include_router(ai_router, prefix="/api")