from PIL import Image as PILImage

from relic.perceptual_hash import phash

def test_phash_returns_hash_for_image(tmp_path):
    image_path = tmp_path / "photo.png"

    image = PILImage.new("RGB", (100, 100))
    image.save(image_path)

    result = phash(image_path)

    assert result is not None