from PIL import Image as PILImage

from relic.perceptual_hash import hamming_distance, phash


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


def test_phash_distinguishes_different_images(tmp_path):
    first_path = tmp_path / "first.png"
    second_path = tmp_path / "second.png"

    first = PILImage.new("RGB", (100, 100), "white")
    first.save(first_path)

    second = PILImage.new("RGB", (100, 100), "black")
    second.save(second_path)

    assert phash(first_path) != phash(second_path)


def test_hamming_distance_is_zero_for_identical_hashes(tmp_path):
    image_path = tmp_path / "photo.png"

    image = PILImage.new("RGB", (100, 100), "white")
    image.save(image_path)

    image_hash = phash(image_path)

    assert hamming_distance(image_hash, image_hash) == 0


def test_hamming_distance_is_low_for_similar_images(tmp_path):
    original_path = tmp_path / "original.png"
    modified_path = tmp_path / "modified.png"

    original = PILImage.new("RGB", (200, 200), "white")
    original.save(original_path)

    modified = original.copy()
    modified.paste("black", (80, 80, 120, 120))
    modified.save(modified_path)

    first_hash = phash(original_path)
    second_hash = phash(modified_path)

    distance = hamming_distance(first_hash, second_hash)

    assert distance < 10