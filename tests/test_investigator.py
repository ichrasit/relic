from datetime import datetime
from pathlib import Path

from relic.image import Image
from relic.image_metadata import ImageMetaData
from relic.image_uploader import ImageUploader
from relic.investigator import Investigator
from relic.search_provider import SearchProvider
from relic.search_result import SearchResult


class FakeImageUploader(ImageUploader):
    def upload(self, image: Image) -> str:
        return "https://example.com/uploaded/photo.jpg"


class FakeSearchProvider(SearchProvider):
    def search(self, image_url: str) -> list[SearchResult]:
        return [
            SearchResult(
                url="https://example.com/photo.jpg",
                title="Example photo",
                source="Example",
                discovered_at=datetime.now(),
                match_score=0.98,
            )
        ]


def create_image() -> Image:
    return Image(
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


def test_investigator_delegates_search_to_provider():
    image = create_image()

    provider = FakeSearchProvider()
    uploader = FakeImageUploader()

    investigator = Investigator(provider, uploader)

    results = investigator.investigate(image)

    assert len(results) == 1
    assert results[0].url == "https://example.com/photo.jpg"


def test_investigator_returns_all_search_results():
    image = create_image()

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

    investigator = Investigator(
        FakeProvider(),
        FakeImageUploader(),
    )

    results = investigator.investigate(image)

    assert len(results) == 2
    assert results[0].url == "https://example.com/one.jpg"
    assert results[1].url == "https://example.com/two.jpg"