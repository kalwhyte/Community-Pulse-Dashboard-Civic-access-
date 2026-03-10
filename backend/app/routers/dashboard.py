from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import DataPoint, Mismatch

router = APIRouter()

# comment: Get a summary of the dashboard data
@router.get("/dashboard/summary")
def get_summary(db: Session = Depends(get_db)):
    count = db.query(DataPoint).count()
    return {"total_data_points": count}

# comment: The above code defines two API endpoints for a dashboard. The first endpoint, "/dashboard/summary", returns the total number of data points in the database. The second endpoint, "/dashboard/mismatches", returns all mismatch records.
@router.get("/dashboard/mismatches")
def get_mismatches(db: Session = Depends(get_db)):
    return db.query(Mismatch).all()
