from pathlib import Path

from relic.image import Image
from relic.image_metadata import ImageMetaData
from relic.image_uploader import ImageUploader


class FakeImageUploader(ImageUploader):
    def upload(self, image: Image) -> str:
        return "https://example.com/uploaded/photo.jpg"


def test_image_uploader_returns_image_url():
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

    uploader = FakeImageUploader()

    assert uploader.upload(image) == "https://example.com/uploaded/photo.jpg"