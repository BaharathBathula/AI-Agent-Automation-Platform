from app.api.v1.routes_runs import router as runs_router

app.include_router(runs_router, prefix="/api/v1", tags=["Runs"])
