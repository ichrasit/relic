import os

def get_serp_api_key() -> str:
    key = os.getenv("SERPAPI_API_KEY")

    if not key:
        raise RuntimeError("SERPAPI_API_KEY is not set")
    return key