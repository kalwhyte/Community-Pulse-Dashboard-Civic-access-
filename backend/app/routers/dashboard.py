from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import DataPoint, Mismatch

router = APIRouter()

@router.get("/dashboard/summary")
def get_summary(db: Session = Depends(get_db)):
    count = db.query(DataPoint).count()
    return {"total_data_points": count}

@router.get("/dashboard/mismatches")
def get_mismatches(db: Session = Depends(get_db)):
    return db.query(Mismatch).all()
