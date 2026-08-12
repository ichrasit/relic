from datetime import datetime

import httpx

from relic.config import get_serp_api_key
from relic.search.result import SearchResult

SERPAPI_URL = "https://serpapi.com/search.json"


class SerpApiProvider:

    def __init__(self, client: httpx.Client | None = None):
        self.client = client or httpx.Client(timeout=30.0)

    def search(self, image_url: str) -> list[SearchResult]:
        params = {
            "engine": "google_lens",
            "url": image_url,
            "type": "all",
            "api_key": get_serp_api_key(),
        }

        response = self.client.get(SERPAPI_URL, params=params)
        response.raise_for_status()

        data = response.json()

        results = []

        for match in data.get("visual_matches", []):
            link = match.get("link")

            if not link:
                continue

            results.append(
                SearchResult(
                    url=link,
                    title=match.get("title", ""),
                    source=match.get("source", ""),
                    discovered_at=datetime.now(),
                    match_score=match.get("match_score", 0.0),
                )
            )

        return results