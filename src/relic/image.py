from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class ImageMetaData:
    width: int 
    height: int
    format: str
    mode: str


@dataclass(frozen=True)
class Image:
    path: Path
    metadata: ImageMetaData
    sha256: str
    phash: str