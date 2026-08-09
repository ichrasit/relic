from pathlib import Path
from relic.filesystem import file_exists, is_image
from PIL import Image as PILImage
def test_file_exists_for_existing_file(tmp_path):
    file_path = tmp_path / "photo.jpg"
    file_path.touch()

    assert file_exists(file_path)

def test_file_exists_for_missing_file(tmp_path):
    file_path = tmp_path / "missing.jpg"
    assert not file_exists(file_path)

def test_file_exists_for_directoru(tmp_path):
    directory = tmp_path / "photos"
    directory.mkdir()

    assert not file_exists(directory)

def test_file_exists_for_valid_image(tmp_path):
    image_path = tmp_path / "photo.jpg"

    image = PILImage.new("RGB", (100, 100))
    image.save(image_path)
    assert file_exists(image_path)

def test_is_image_for_valid_image(tmp_path):
    image_path = tmp_path / "photo.png"

    image = PILImage.new("RGB", (100, 100))
    image.save(image_path)

    assert is_image(image_path)

def test_is_image_for_invalid_file(tmp_path):
    file_path = tmp_path / "not-an-image.txt"
    file_path.write_text("this is definetly not an image")

    assert not is_image(file_path)

def test_is_image_for_directory(tmp_path):
    directory = tmp_path / "photos"
    directory.mkdir()

    assert not is_image(directory)

def test_is_image_for_corrupted_image(tmp_path):
    image_path = tmp_path / "corrupted.png"
    image_path.write_bytes(b"\x89PNG\r\n\x1a\nbroken")

    assert not is_image(image_path)

