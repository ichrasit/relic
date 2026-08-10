from datetime import datetime
from pathlib import Path

from relic.image import Image
from relic.image_metadata import ImageMetaData
from relic.search_provider import SearchProvider
from relic.search_result import SearchResult


class FakeSearchProvider(SearchProvider):

    def search(self, image: Image) -> list[SearchResult]:
        return [
            SearchResult(
                url="https://example.com/photo.jpg",
                title="Example photo",
                source="example",
                discovered_at=datetime.now(),
                match_score=0.98,
            )
        ]


def test_search_provider_returns_results():
    image = Image(
        path=Path("/tmp/photo.jpg"),
        metadata=ImageMetaData(
            width=100,
            height=100,
            format="JPEG",
            mode="RGB",
        ),
        sha256="abc",
        phash="0000000000000000",
    )

    provider = FakeSearchProvider()

    results = provider.search(image)

    assert len(results) == 1
    assert results[0].url == "https://example.com/photo.jpg"