import re
import requests

from ..config import (
    BRIGHT_DATA_API_KEY,
    BRIGHT_DATA_DATASET_ID,
    BRIGHT_DATA_REDDIT_DATASET_ID,
)

SCRAPE_URL = "https://api.brightdata.com/datasets/v3/scrape"
PROGRESS_URL = "https://api.brightdata.com/datasets/v3/progress/{snapshot_id}"
SNAPSHOT_URL = "https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}"

# Dataset expects X/Twitter status URLs.
_TWITTER_STATUS_RE = re.compile(
    r"^https://(www\.)?(?:x\.com|twitter\.com)/[a-zA-Z0-9_]+/status/\d+/?$"
)

# Reddit dataset can ingest subreddit and post URLs.
_REDDIT_URL_RE = re.compile(
    r"^https://(www\.)?reddit\.com/r/[a-zA-Z0-9_]+(?:/|$)"
)


def _get_headers():
    if not BRIGHT_DATA_API_KEY:
        raise ValueError("BRIGHT_DATA_API_KEY is not set")
    return {
        "Authorization": f"Bearer {BRIGHT_DATA_API_KEY}",
        "Content-Type": "application/json",
    }


def _normalize_url(url) -> str:
    url = str(url).strip()
    if not url:
        return url
    if url.startswith("http://") or url.startswith("https://"):
        return url
    return f"https://{url}"


def _classify_urls(urls):
    x_urls = [url for url in urls if _TWITTER_STATUS_RE.match(url)]
    reddit_urls = [url for url in urls if _REDDIT_URL_RE.match(url)]
    unknown_urls = [url for url in urls if url not in x_urls and url not in reddit_urls]
    return x_urls, reddit_urls, unknown_urls


def crawl_data(url: str):
    headers = _get_headers()
    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()


def _post_scrape(dataset_id: str, urls, timeout_seconds: int = 180):
    if not dataset_id:
        raise ValueError("Dataset ID is not set")

    params = {
        "dataset_id": dataset_id,
        "include_errors": "true",
    }

    payload = {
        "input": [{"url": url} for url in urls]
    }

    response = requests.post(
        SCRAPE_URL,
        headers=_get_headers(),
        params=params,
        json=payload,
        timeout=timeout_seconds,
    )

    if not response.ok:
        raise requests.HTTPError(
            f"{response.status_code} Client Error: {response.text}",
            response=response,
        )

    return response.json()


# Define a function to trigger a crawl job.
def trigger_crawl(urls):
    if not urls:
        raise ValueError("urls must contain at least one URL")

    normalized_urls = [_normalize_url(url) for url in urls]
    x_urls, reddit_urls, unknown_urls = _classify_urls(normalized_urls)

    if unknown_urls:
        raise ValueError(
            "Unsupported URLs detected. Supported patterns: "
            "X/Twitter status URLs like https://x.com/user/status/1234567890 and "
            "Reddit subreddit URLs like https://www.reddit.com/r/montgomery/"
        )

    if x_urls and reddit_urls:
        raise ValueError(
            "Mixed sources detected. Please submit X/Twitter and Reddit URLs in separate requests."
        )

    if x_urls:
        return _post_scrape(BRIGHT_DATA_DATASET_ID, x_urls, timeout_seconds=180)

    if reddit_urls:
        return _post_scrape(BRIGHT_DATA_REDDIT_DATASET_ID, reddit_urls, timeout_seconds=180)

    raise ValueError("No valid URLs found")


# Define a function to check crawl progress.
def get_progress(snapshot_id):
    if not snapshot_id:
        raise ValueError("snapshot_id is required")

    endpoint = PROGRESS_URL.format(snapshot_id=snapshot_id)
    response = requests.get(endpoint, headers=_get_headers(), timeout=60)
    response.raise_for_status()
    return response.json()


# Define a function to download a completed snapshot.
def download_snapshot(snapshot_id, format_type="json"):
    if not snapshot_id:
        raise ValueError("snapshot_id is required")

    endpoint = SNAPSHOT_URL.format(snapshot_id=snapshot_id)
    params = {"format": format_type}
    response = requests.get(endpoint, headers=_get_headers(), params=params, timeout=120)
    response.raise_for_status()
    return response.json()