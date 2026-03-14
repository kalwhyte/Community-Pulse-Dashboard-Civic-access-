import os
from pathlib import Path


def _load_dotenv():
    env_path = Path(__file__).resolve().parents[1] / ".env"
    if not env_path.exists():
        return
    for line in env_path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if "=" not in line:
            continue
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip().strip('"').strip("'")
        if key and key not in os.environ:
            os.environ[key] = value


_load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@localhost/community_pulse")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Bright Data
BRIGHT_DATA_API_KEY = os.getenv("BRIGHT_DATA_API_KEY")
BRIGHT_DATA_DATASET_ID = os.getenv("BRIGHT_DATA_DATASET_ID")
BRIGHT_DATA_REDDIT_DATASET_ID = os.getenv("BRIGHT_DATA_REDDIT_DATASET_ID")

# Backwards-compatible aliases without underscore (if referenced elsewhere)
BRIGHTDATA_API_KEY = BRIGHT_DATA_API_KEY
BRIGHTDATA_DATASET_ID = BRIGHT_DATA_DATASET_ID
BRIGHTDATA_REDDIT_DATASET_ID = BRIGHT_DATA_REDDIT_DATASET_ID