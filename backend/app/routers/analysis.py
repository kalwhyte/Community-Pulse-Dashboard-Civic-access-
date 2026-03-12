from fastapi import APIRouter

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

    # Return the snapshot ID in a clean response.
    return CrawlResponse(snapshot_id=result["snapshot_id"])