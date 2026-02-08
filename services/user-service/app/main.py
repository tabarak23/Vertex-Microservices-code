from fastapi import FastAPI
from app.api.v1.user_controller import router
from app.core.metrics import setup_metrics
from app.core.config import settings
import app.core.logging

from app.db.init_db import init_db  # 👈 ADD THIS

app = FastAPI(title="User Service", version="1.0.0")

# Metrics
setup_metrics(app)

# Routes
app.include_router(router, prefix="/api/v1/users")

# DB init (CRITICAL)
@app.on_event("startup")
def on_startup():
    init_db()

@app.get("/health")
def health():
    return {"status": "ok"}

