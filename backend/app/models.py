# Import Column so we can define table columns.
from sqlalchemy import Column

# Import Integer for numeric ID fields.
from sqlalchemy import Integer

# Import String for text fields.
from sqlalchemy import String

# Import Float for score values.
from sqlalchemy import Float

# Import DateTime for timestamps.
from sqlalchemy import DateTime

# Import Text for longer text content.
from sqlalchemy import Text

# Import func so we can use database-side defaults like current timestamp.
from sqlalchemy.sql import func

# Import the shared Base from our database module.
from app.database import Base

# Define the table for social media posts.
class SocialPost(Base):
    # Set the SQL table name.
    __tablename__ = "social_posts"

    # Define the primary key ID column.
    id = Column(Integer, primary_key=True, index=True)

    # Store the source platform, such as Twitter or Reddit.
    source = Column(String, nullable=False)

    # Store the original post URL.
    url = Column(String, nullable=False)

    # Store the post text content.
    content = Column(Text, nullable=False)

    # Store the detected location or district.
    location = Column(String, nullable=True)

    # Store the issue category, such as crime or roads.
    category = Column(String, nullable=True)

    # Store the sentiment label.
    sentiment = Column(String, nullable=True)

    # Store the numeric sentiment score.
    sentiment_score = Column(Float, nullable=True)

    # Store the creation timestamp.
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Define the table for official city reports.
class OfficialReport(Base):
    # Set the SQL table name.
    __tablename__ = "official_reports"

    # Define the primary key ID column.
    id = Column(Integer, primary_key=True, index=True)

    # Store the source dataset name.
    dataset_name = Column(String, nullable=False)

    # Store the issue category.
    category = Column(String, nullable=False)

    # Store the location or district.
    location = Column(String, nullable=False)

    # Store the total number of incidents or requests.
    count = Column(Integer, nullable=False, default=0)

    # Store the timestamp.
    created_at = Column(DateTime(timezone=True), server_default=func.now())

# Define the table for mismatch scores.
class MismatchScore(Base):
    # Set the SQL table name.
    __tablename__ = "mismatch_scores"

    # Define the primary key ID column.
    id = Column(Integer, primary_key=True, index=True)

    # Store the district or location.
    location = Column(String, nullable=False)

    # Store the issue category.
    category = Column(String, nullable=False)

    # Store the aggregated social sentiment score.
    social_score = Column(Float, nullable=False)

    # Store the aggregated official activity score.
    official_score = Column(Float, nullable=False)

    # Store the computed mismatch score.
    mismatch_score = Column(Float, nullable=False)

    # Store the AI-generated explanation.
    explanation = Column(Text, nullable=True)

    # Store the timestamp.
    created_at = Column(DateTime(timezone=True), server_default=func.now())