import os

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/community_pulse")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
BRIGHT_DATA_API_KEY = os.getenv("BRIGHT_DATA_API_KEY")
