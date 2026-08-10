from pathlib import Path
import imagehash
from PIL import Image as PILImage


def phash(path: Path) -> imagehash.ImageHash:
    with PILImage.open(path) as image:
        return imagehash.phash(image)

def hamming_distance(
        first: imagehash.ImageHash,
        second: imagehash.ImageHash,
) -> int:
    return first - second