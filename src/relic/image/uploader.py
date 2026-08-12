from abc import ABC, abstractmethod

from relic.image import Image

class ImageUploader(ABC):
    @abstractmethod
    def upload(self, image: Image) -> str:
        ...