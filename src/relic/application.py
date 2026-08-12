from pathlib import Path

from relic.image_loader import ImageLoader
from relic.investigator import Investigator
from relic.search_result import SearchResult

class RelicApplication:
    def __init__(self, investigator: Investigator):
        self.investigator = investigator

    def investigate(self, path: Path) -> list[SearchResult]:
        image = ImageLoader.load(path)
        return self.investigator.investigate(image)

    