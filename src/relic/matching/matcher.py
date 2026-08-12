from pathlib import Path

from relic.image import Image
from relic.image.loader import ImageLoader
from relic.matching.scorer import phash_similarity
from relic.matching.fetcher import ImageFetcher


class ImageMatcher:
    def __init__(
        self,
        fetcher: ImageFetcher | None = None,
        loader: ImageLoader | None = None,
    ):
        self.fetcher = fetcher or ImageFetcher()
        self.loader = loader or ImageLoader()

    def match(
        self,
        source: Image,
        candidate_url: str,
        destination: Path,
    ) -> float:
        candidate_path = self.fetcher.fetch(
            candidate_url,
            destination,
        )

        candidate = self.loader.load(candidate_path)

        return phash_similarity(
            source.phash,
            candidate.phash,
        )