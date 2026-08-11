from relic.image import Image
from relic.search_provider import SearchProvider
from relic.search_result import SearchResult


class Investigator:
    def __init__(self, provider: SearchProvider):
        self.provider = provider

    def investigate(self, image: Image) -> list[SearchResult]:
        return self.provider.search(str(image.path))