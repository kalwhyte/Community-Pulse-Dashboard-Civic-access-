from fastapi import APIRouter
from app.schemas import InsightResponse

# Create a router for dashboard-related endpoints.
router = APIRouter(prefix="/dashboard", tags=["Dashboard"])


# Define a sample summary route for the frontend.
@router.get("/summary")
def get_summary():
    # Return a simple mock response for the dashboard cards.
    return {
        "city": "Montgomery",
        "top_issue": "Road Infrastructure",
        "average_sentiment": -0.42,
        "mismatch_hotspots": 4,
    }

# Define a sample insights route for the frontend.
@router.get("/insights", response_model=list[InsightResponse])
def get_insights():
    # Return a list of sample insight records.
    return [
        InsightResponse(
            location="Midtown",
            category="Road Infrastructure",
            social_score=0.82,
            official_score=0.21,
            mismatch_score=0.61,
            explanation="Residents are discussing worsening potholes online, but official reports remain relatively low."
        )
    ]