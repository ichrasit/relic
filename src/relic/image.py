from dataclasses import dataclass
from pathlib import Path

from relic.image_metadata import ImageMetaData


@dataclass(frozen=True)
class Image:
    path: Path
    metadata: ImageMetaData
    sha256: str
    phash: str