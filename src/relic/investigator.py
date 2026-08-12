from relic.image import Image
from relic.image_uploader import ImageUploader
from relic.search_provider import SearchProvider
from relic.search_result import SearchResult


class Investigator:
    def __init__(
        self,
        provider: SearchProvider,
        uploader: ImageUploader,
    ):
        self.provider = provider
        self.uploader = uploader

    def investigate(self, image: Image) -> list[SearchResult]:
        image_url = self.uploader.upload(image)
        return self.provider.search(image_url)