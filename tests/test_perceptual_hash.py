from PIL import Image as PILImage

from relic.perceptual_hash import phash

def test_phash_returns_hash_for_image(tmp_path):
    image_path = tmp_path / "photo.png"

    image = PILImage.new("RGB", (100, 100))
    image.save(image_path)

    result = phash(image_path)

    assert result is not None


def test_phash_is_deterministic(tmp_path):
    image_path = tmp_path / "photo.png"

    image = PILImage.new("RGB", (100, 100), "white")
    image.save(image_path)

    first = phash(image_path)
    second = phash(image_path)

    assert first == second


def test_phash_matches_resized_image(tmp_path):
    original_path = tmp_path / "original.png"
    resized_path = tmp_path / "resized.png"

    original = PILImage.new("RGB", (100, 100), "white")
    original.save(original_path)

    resized = original.resize((500, 500))
    resized.save(resized_path)

    assert phash(original_path) == phash(resized_path)