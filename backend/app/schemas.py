# Import BaseModel from Pydantic for request and response validation.
from pydantic import BaseModel, HttpUrl

# Import List to type arrays of values.
from typing import List

# Define the schema for a crawl request.
class CrawlRequest(BaseModel):
    # Accept a list of URLs to crawl.
    urls: List[HttpUrl]

# Define the response schema for a crawl trigger.
class CrawlResponse(BaseModel):
    # Return the Bright Data snapshot ID.
    snapshot_id: str

# Define the schema for dashboard insight data.
class InsightResponse(BaseModel):
    # The name of the location being analyzed.
    location: str

    # The issue category.
    category: str

    # The social sentiment score.
    social_score: float

    # The official activity score.
    official_score: float

    # The mismatch score.
    mismatch_score: float

    # The AI-generated explanation.
    explanation: str