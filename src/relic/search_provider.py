from abc import ABC, abstractclassmethod

from relic.image import Image
from relic.search_result import SearchResult


class SearchProvider(ABC):
    @abstractclassmethod
    def search(self, image: Image) -> list[SearchResult]:
     ...

