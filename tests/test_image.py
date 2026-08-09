from pathlib import Path

from relic.image import Image, ImageMetaData

def test_image_stores_path():
    path = Path("/tmp/photo.jpgj")

    metadata = ImageMetaData(
        width = 1920,
        height = 1080,
        format = "JPEG",
        mode="RGB",
    )
    image = Image(path, metadata)
    assert image.path == path


def test_image_stores_metadata():
    metadata = ImageMetaData(
        width = 1920,
        height = 1080,
        format = "JPEG",
        mode = "RGB",
    )
    image = Image(Path("/tmp/photo.jpg"), metadata)


    assert image.metadata == metadata

def test_image_path_is_object():
    image = Image(
        Path("/tmp/photo.jpg"),
        ImageMetaData(
            width = 100,
            height = 100,
            format = "PNG",
            mode = "RGB",
        )
    )

    assert isinstance(image.path, Path)


def test_image_is_immutable():
    image = Image(
        Path("/tmp/photo.jpg"),
        ImageMetaData(
            width = 100,
            height = 100,
            format = "PNG",
            mode = "RGB",
        )
    )
    try:
        image.path = Path("/tmp/other.jpg")
    except AttributeError:
        pass
    else:
        raise AssertionError("Image should be immutable")

    

def test_image_metadata_is_immutable():
    metadata = ImageMetaData(
        width = 1920,
        height = 1080,
        format = "JPEG",
        mode = "RGB",
    )

    try:
        metadata.width = 800
    except AttributeError:
        pass
    else:
        raise AssertionError("ImageMetadata should be immutable")
