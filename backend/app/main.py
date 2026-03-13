from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .routers import ingest, dashboard, analysis

app = FastAPI(title="Community Pulse API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # Next.js dev server
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(ingest.router, prefix="/api/v1")
app.include_router(dashboard.router, prefix="/api/v1")
app.include_router(analysis.router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "Community Pulse Backend"}