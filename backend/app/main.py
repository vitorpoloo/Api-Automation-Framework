from fastapi import FastAPI

from app.api.routes.health import router as health_router


app = FastAPI(
    title="API Automation Framework",
    description="API automation platform",
    version="1.0.0",
)

app.include_router(health_router)