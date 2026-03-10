from pydantic import BaseModel
from datetime import datetime

class DataPointBase(BaseModel):
    source: str
    content: str
    latitude: float
    longitude: float

class DataPointCreate(DataPointBase):
    pass

class DataPoint(DataPointBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class MismatchBase(BaseModel):
    description: str
    data_point_id: int

class MismatchCreate(MismatchBase):
    pass

class Mismatch(MismatchBase):
    id: int

    class Config:
        orm_mode = True
