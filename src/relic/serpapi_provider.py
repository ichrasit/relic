import httpx
from relic.config import get_serp_api_key
from relic.image import Image
from relic.search_result import SearchResult

SERPAPI_URL = "https://serpapi.com/search.json"

class SerpApiProvider:
    def __init__(self, client: httpx.Client | None = None):
        self.client = client or httpx.Client(timeout=30.0)

    def search(self, image_url: str) -> dict:
        params = {
            "engine": "google_lens",
            "url": image_url,
            "type": "all",
            "api_key": get_serpapi_api_key(),
        }

        response = self.client.get(SERPAPI_URL, params=params)
        response.raise_for_status()

        return response.json()