from pathlib import Path

from relic.image.loader import ImageLoader
from relic.investigation.investigator import Investigator
from relic.search.result import SearchResult

class RelicApplication:
    def __init__(self, investigator: Investigator):
        self.investigator = investigator

    def investigate(self, path: Path) -> list[SearchResult]:
        image = ImageLoader.load(path)
        return self.investigator.investigate(image)

    