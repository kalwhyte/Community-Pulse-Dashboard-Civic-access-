import requests

from ..config import GEMINI_API_KEY

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent"


def analyze_post_with_gemini(content):
    if not GEMINI_API_KEY:
        raise ValueError("GEMINI_API_KEY is not set")
    if not content:
        raise ValueError("content is required")

    endpoint = f"{API_URL}?key={GEMINI_API_KEY}"

    prompt = f"""
    Analyze the following social media post.
    Return only valid JSON with these keys:
    category, sentiment, sentiment_score, location, summary

    Post:
    {content}
    """

    payload = {
        "contents": [
            {
                "parts": [
                    {
                        "text": prompt
                    }
                ]
            }
        ]
    }

    response = requests.post(endpoint, json=payload, timeout=60)
    response.raise_for_status()
    return response.json()