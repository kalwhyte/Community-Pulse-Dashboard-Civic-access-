import re
import requests

from ..config import BRIGHT_DATA_API_KEY, BRIGHT_DATA_DATASET_ID

SCRAPE_URL = "https://api.brightdata.com/datasets/v3/scrape"
PROGRESS_URL = "https://api.brightdata.com/datasets/v3/progress/{snapshot_id}"
SNAPSHOT_URL = "https://api.brightdata.com/datasets/v3/snapshot/{snapshot_id}"

# Dataset expects X/Twitter status URLs.
_TWITTER_STATUS_RE = re.compile(
    r"^https://(www\.)?(?:x\.com|twitter\.com)/(?:[a-zA-Z0-9_]+/)?status|statuses/\d+$"
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


def _validate_urls(urls):
    invalid = [url for url in urls if not _TWITTER_STATUS_RE.match(url)]
    if invalid:
        raise ValueError(
            "Bright Data dataset only accepts X/Twitter status URLs. "
            "Example: https://x.com/user/status/1234567890"
        )


def crawl_data(url: str):
    headers = _get_headers()
    response = requests.get(url, headers=headers, timeout=60)
    response.raise_for_status()
    return response.json()


# Define a function to trigger a crawl job.
def trigger_crawl(urls):
    if not BRIGHT_DATA_DATASET_ID:
        raise ValueError("BRIGHT_DATA_DATASET_ID is not set")
    if not urls:
        raise ValueError("urls must contain at least one URL")

    # Normalize URLs to include a scheme.
    normalized_urls = [_normalize_url(url) for url in urls]
    _validate_urls(normalized_urls)

    # Build query parameters required by Bright Data.
    params = {
        "dataset_id": BRIGHT_DATA_DATASET_ID,
        "include_errors": "true",
        "custom_output_fields": "markdown|html",
    }

    # Build the request body as a list of URL objects.
    payload = {
        "input": [{"url": url} for url in normalized_urls]
    }

    # Send the POST request to Bright Data.
    response = requests.post(SCRAPE_URL, headers=_get_headers(), params=params, json=payload, timeout=60)

    if not response.ok:
        raise requests.HTTPError(
            f"{response.status_code} Client Error: {response.text}",
            response=response,
        )

    # Return the JSON body from Bright Data.
    return response.json()


# Define a function to check crawl progress.
def get_progress(snapshot_id):
    if not snapshot_id:
        raise ValueError("snapshot_id is required")

    # Build the progress endpoint URL.
    endpoint = PROGRESS_URL.format(snapshot_id=snapshot_id)

    # Send the GET request.
    response = requests.get(endpoint, headers=_get_headers(), timeout=60)

    # Raise an exception if the call fails.
    response.raise_for_status()

    # Return the JSON progress data.
    return response.json()


# Define a function to download a completed snapshot.
def download_snapshot(snapshot_id, format_type="json"):
    if not snapshot_id:
        raise ValueError("snapshot_id is required")

    # Build the snapshot endpoint URL.
    endpoint = SNAPSHOT_URL.format(snapshot_id=snapshot_id)

    # Set the query parameters for downloading the snapshot.
    params = {
        "format": format_type,
    }

    # Send the GET request to Bright Data.
    response = requests.get(endpoint, headers=_get_headers(), params=params, timeout=120)

    # Raise an exception if the call fails.
    response.raise_for_status()

    # Return the parsed JSON response.
    return response.json()