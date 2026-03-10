from sqlalchemy import Column, Integer, String, DateTime, Float
from .database import Base

class DataPoint(Base):
    __tablename__ = "data_points"

    id = Column(Integer, primary_key=True, index=True)
    source = Column(String, index=True)
    content = Column(String)
    timestamp = Column(DateTime)
    latitude = Column(Float)
    longitude = Column(Float)

class Mismatch(Base):
    __tablename__ = "mismatches"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String)
    data_point_id = Column(Integer)
