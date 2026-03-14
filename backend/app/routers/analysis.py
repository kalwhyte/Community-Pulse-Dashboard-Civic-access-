from fastapi import APIRouter

# Create a router for analysis endpoints.
router = APIRouter(prefix="/analysis", tags=["Analysis"])


@router.get("/health")
def analysis_health():
    return {"status": "ok"}