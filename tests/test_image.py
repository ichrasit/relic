from pathlib import Path

from PIL import Image as PILImage

from relic.image import Image
from relic.image_loader import ImageLoader
from relic.image_metadata import ImageMetaData
from relic.perceptual_hash import phash


def test_image_stores_path():
    path = Path("/tmp/photo.jpg")

    metadata = ImageMetaData(
        width=1920,
        height=1080,
        format="JPEG",
        mode="RGB",
    )

    image = Image(path, metadata, "abc123", "0000000000000000")

    assert image.path == path


def test_image_stores_metadata():
    metadata = ImageMetaData(
        width=1920,
        height=1080,
        format="JPEG",
        mode="RGB",
    )

    image = Image(
        Path("/tmp/photo.jpg"),
        metadata,
        "abc123",
        "0000000000000000",
    )

    assert image.metadata == metadata


def test_image_path_is_object():
    image = Image(
        Path("/tmp/photo.jpg"),
        ImageMetaData(
            width=100,
            height=100,
            format="PNG",
            mode="RGB",
        ),
        "abc123",
        "0000000000000000",
    )

    assert isinstance(image.path, Path)


def test_image_is_immutable():
    image = Image(
        Path("/tmp/photo.jpg"),
        ImageMetaData(
            width=100,
            height=100,
            format="PNG",
            mode="RGB",
        ),
        "abc123",
        "0000000000000000",
    )

    try:
        image.path = Path("/tmp/other.jpg")
    except AttributeError:
        pass
    else:
        raise AssertionError("Image should be immutable")


def test_image_metadata_is_immutable():
    metadata = ImageMetaData(
        width=1920,
        height=1080,
        format="JPEG",
        mode="RGB",
    )

    try:
        metadata.width = 800
    except AttributeError:
        pass
    else:
        raise AssertionError("ImageMetadata should be immutable")


def test_image_stores_sha256():
    image = Image(
        Path("/tmp/photo.jpg"),
        ImageMetaData(
            width=1920,
            height=1080,
            format="JPEG",
            mode="RGB",
        ),
        "abc123",
        "0000000000000000",
    )

    assert image.sha256 == "abc123"


def test_image_stores_phash(tmp_path):
    image_path = tmp_path / "photo.png"

    source = PILImage.new("RGB", (100, 100), "white")
    source.save(image_path)

    image = ImageLoader.load(image_path)

    assert image.phash == str(phash(image_path))