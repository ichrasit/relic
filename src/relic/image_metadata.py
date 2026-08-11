from dataclasses import dataclass

@dataclass(frozen=True)
class ImageMetaData:
    width: int
    height: int
    format: str
    mode: str