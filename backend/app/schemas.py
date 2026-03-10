from pydantic import BaseModel
from datetime import datetime

# commeent: Define Pydantic models for data validation and serialization
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
        from_attributes = True

# comment: Define Pydantic models for mismatch records
class MismatchBase(BaseModel):
    description: str
    data_point_id: int

class MismatchCreate(MismatchBase):
    pass

class Mismatch(MismatchBase):
    id: int

    class Config:
        from_attributes = True
