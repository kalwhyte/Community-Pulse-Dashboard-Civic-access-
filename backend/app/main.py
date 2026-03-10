from fastapi import FastAPI
from .routers import ingest, dashboard, analysis

app = FastAPI(title="Community Pulse API")

app.include_router(ingest.router, prefix="/api/v1", tags=["ingest"])
app.include_router(dashboard.router, prefix="/api/v1", tags=["dashboard"])
app.include_router(analysis.router, prefix="/api/v1", tags=["analysis"])

@app.get("/")
def root():
    return {"message": "Community Pulse Backend"}
