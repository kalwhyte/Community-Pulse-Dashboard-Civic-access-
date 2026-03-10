from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database import get_db
from ..models import DataPoint
from ..schemas import DataPointCreate, DataPoint

router = APIRouter()

@router.post("/ingest", response_model=DataPoint)
def ingest_data(data: DataPointCreate, db: Session = Depends(get_db)):
    db_item = DataPoint(**data.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/data", response_model=list[DataPoint])
def get_data(db: Session = Depends(get_db)):
    return db.query(DataPoint).all()
