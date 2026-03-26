from fastapi import FastAPI
from app.api.v1.routes_health import router as health_router
from app.api.v1.routes_tasks import router as tasks_router

app = FastAPI(
    title="AI Agent & Automation Platform",
    version="0.1.0",
    description="Production-grade AI agent and automation system with workflow orchestration, tool calling, memory, scheduling, and observability."
)

app.include_router(health_router, prefix="/api/v1", tags=["Health"])
app.include_router(tasks_router, prefix="/api/v1", tags=["Tasks"])


@app.get("/")
def root():
    return {
        "message": "AI Agent & Automation Platform is running",
        "docs": "/docs"
    }
