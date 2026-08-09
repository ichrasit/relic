from pathlib import Path

import pytest
from PIL import Image as PILImage
from relic.fingerprint import sha256

from relic.image import Image, ImageMetaData
from relic.image_loader import ImageLoader


def test_load_png_image(tmp_path):
    image_path = tmp_path / "photo.png"

    source = PILImage.new("RGB", (800, 600))
    source.save(image_path)

    image = ImageLoader.load(image_path)

    assert isinstance(image, Image)
    assert image.path == image_path
    assert image.metadata == ImageMetaData(
        width=800,
        height=600,
        format="PNG",
        mode="RGB",
    )


def test_load_jpeg_image(tmp_path):
    image_path = tmp_path / "photo.jpg"

    source = PILImage.new("RGB", (1920, 1080))
    source.save(image_path, format="JPEG")

    image = ImageLoader.load(image_path)

    assert image.metadata.width == 1920
    assert image.metadata.height == 1080
    assert image.metadata.format == "JPEG"
    assert image.metadata.mode == "RGB"



def test_load_invalid_file(tmp_path):
    file_path = tmp_path / "not-an-image.txt"
    file_path.write_text("this is not an image")

    with pytest.raises(ValueError, match="Invalid image file"):
        ImageLoader.load(file_path)


def test_load_missing_file(tmp_path):
    image_path = tmp_path / "missing.jpg"

    with pytest.raises(ValueError, match="Invalid image file"):
        ImageLoader.load(image_path)


def test_load_generates_sha256(tmp_path):
    image_path = tmp_path / "photo.jpg"

    source = PILImage.new("RGB", (100, 100))
    source.save(image_path)

    image = ImageLoader.load(image_path)

    assert len(image.sha256) == 64


def test_load_generates_correct_sha256(tmp_path):
    image_path = tmp_path / "photo.png"

    source = PILImage.new("RGB", (100, 100))
    source.save(image_path)

    image = ImageLoader.load(image_path)

    assert image.sha256 == sha256(image_path)


def test_same_image_has_same_sha256(tmp_path):
    image_path = tmp_path / "photo.png"

    source = PILImage.new("RGB", (100, 100))
    source.save(image_path)

    first = ImageLoader.load(image_path)
    second = ImageLoader.load(image_path)

    assert first.sha256 == second.sha256

    