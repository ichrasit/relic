from dataclasses import dataclass


@dataclass(frozen=True)
class ImageFeatures:
    phash: str
    width: int
    height: int
    aspect_ratio: float


def extract_features(image) -> ImageFeatures:
    width = image.metadata.width
    height = image.metadata.height

    return ImageFeatures(
        phash=image.phash,
        width=width,
        height=height,
        aspect_ratio=width / height,
    )