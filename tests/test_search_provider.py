from relic.search_provider import SearchProvider
from relic.search_result import SearchResult
from datetime import datetime

class FakeSearchProvider(SearchProvider):
    def search(self, image_url: str) -> list[SearchResult]:
        return [
            SearchResult(
                url="https://example.com/photo.jpg",
                title="Example photo",
                source="example",
                discovered_at=datetime.now(),
                match_score=0.98,
            )
        ]