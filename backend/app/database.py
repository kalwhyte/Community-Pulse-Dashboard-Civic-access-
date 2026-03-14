# Import the create_engine function from SQLAlchemy to create database connections
from sqlalchemy import create_engine
# Import declarative_base to create a base class for database models
from sqlalchemy.ext.declarative import declarative_base
# Import sessionmaker to create session factories for database interactions
from sqlalchemy.orm import sessionmaker
# Import the database URL from the config module
from .config import DATABASE_URL

# Create the database engine using the DATABASE_URL
engine = create_engine(DATABASE_URL)
# Create a session factory with autocommit and autoflush disabled, bound to the engine
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base class for all database models
Base = declarative_base()

# Define a dependency function to get a database session
def get_db():
    # Create a new database session
    db = SessionLocal()
    # Use try-finally to ensure the session is closed after use
    try:
        # Yield the session to the caller
        yield db
    finally:
        # Close the session in the finally block
        db.close()
