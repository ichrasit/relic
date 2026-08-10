from pathlib import Path

from relic.image import Image
from relic.image_matcher import match
from relic.image_metadata import ImageMetaData


def test_identical_images_have_full_match():
    image = Image(
        path=Path("/tmp/photo.png"),
        metadata=ImageMetaData(
            width=100,
            height=100,
            format="PNG",
            mode="RGB",
        ),
        sha256="abc",
        phash="0000000000000000",
    )

    assert match(image, image) == 1.0