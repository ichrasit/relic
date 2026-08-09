from pathlib import Path
from PIL import Image as PILImage

from relic.image import Image, ImageMetaData
from relic.filesystem import is_image

class ImageLoader:
    @staticmethod
    def load(path: Path) -> Image:
        if not is_image(path):
            raise ValueError(f"Invalid image file: {path}")
        with PILImage.open(path) as image:
            metadata = ImageMetaData(
                width=image.width,
                height=image.height,
                format=image.format,
                mode=image.mode,
            )

        return Image(path=path, metadata=metadata)