from abc import ABC, abstractmethod

from relic.search_result import SearchResult


class SearchProvider(ABC):
    @abstractmethod
    def search(self, image_url: str) -> list[SearchResult]:
     ...

