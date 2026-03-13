# Import APIRouter so we can define grouped API routes.
from fastapi import APIRouter, HTTPException

# Import the request schema.
from app.schemas import CrawlRequest

# Import the response schema.
from app.schemas import CrawlResponse

# Import the Bright Data trigger function.
from app.services.brightdata_client import trigger_crawl

# Create a router for ingestion endpoints.
router = APIRouter(prefix="/ingest", tags=["Ingestion"])

# Define an endpoint for social crawl triggering.
@router.post("/social", response_model=CrawlResponse)
def ingest_social_data(payload: CrawlRequest):
    # Trigger a Bright Data crawl using the list of URLs.
    result = trigger_crawl(payload.urls)

    snapshot_id = (
        result.get("snapshot_id")
        or result.get("snapshotId")
        or result.get("id")
    )
    if not snapshot_id:
        raise HTTPException(status_code=502, detail=f"Bright Data response missing snapshot_id/id: {result}")

    # Return the snapshot ID in a clean response.
    return CrawlResponse(snapshot_id=str(snapshot_id))