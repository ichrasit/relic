from pathlib import Path

from PIL import Image as PILImage

from relic.application import RelicApplication
from relic.image import Image
from relic.investigator import Investigator
from relic.search_result import SearchResult


class FakeInvestigator:
    def investigate(self, image: Image) -> list[SearchResult]:
        return [
            SearchResult(
                url="https://example.com/photo.jpg",
                title="Example photo",
                source="Example",
                discovered_at=__import__("datetime").datetime.now(),
                match_score=0.98,
            )
        ]


def test_application_loads_image_and_investigates(tmp_path):
    image_path = tmp_path / "photo.png"

    image = PILImage.new("RGB", (100, 100), "white")
    image.save(image_path)

    app = RelicApplication(FakeInvestigator())

    results = app.investigate(image_path)

    assert len(results) == 1
    assert results[0].url == "https://example.com/photo.jpg"