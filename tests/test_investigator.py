from pathlib import Path
from datetime import datetime

from relic.image import Image
from relic.image_metadata import ImageMetaData
from relic.investigator import Investigator
from relic.search_provider import SearchProvider
from relic.search_result import SearchResult


class FakeSearchProvider(SearchProvider):
    def __init__(self):
        self.image_url = None

    def search(self, image_url: str) -> list[SearchResult]:
        self.image_url = image_url

        return [
            SearchResult(
                url="https://example.com/photo.jpg",
                title="Example photo",
                source="Example",
                discovered_at=datetime.now(),
                match_score=1.0,
            )
        ]


def test_investigator_delegates_search_to_provider():
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
    investigator = Investigator(provider)

    results = investigator.investigate(image)

    assert len(results) == 1
    assert results[0].url == "https://example.com/photo.jpg"
    assert provider.image_url == str(image.path)

def test_investigator_returns_all_search_results():
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

    class FakeProvider(SearchProvider):
        def search(self, image_url: str) -> list[SearchResult]:
            return [
                SearchResult(
                    url="https://example.com/one.jpg",
                    title="First result",
                    source="Example",
                    discovered_at=datetime.now(),
                    match_score=0.95,
                ),
                SearchResult(
                    url="https://example.com/two.jpg",
                    title="Second result",
                    source="Example",
                    discovered_at=datetime.now(),
                    match_score=0.80,
                ),
            ]

    investigator = Investigator(FakeProvider())

    results = investigator.investigate(image)

    assert len(results) == 2
    assert results[0].url == "https://example.com/one.jpg"
    assert results[1].url == "https://example.com/two.jpg"