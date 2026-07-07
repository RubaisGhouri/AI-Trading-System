from fastapi import FastAPI

app = FastAPI(title="AI Trading System")


@app.get("/")
def home():
    return {
        "status": "running",
        "project": "AI Trading System",
        "phase": "Phase 1 Complete"
    }