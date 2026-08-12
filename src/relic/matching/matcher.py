from pathlib import Path

from relic.image import Image
from relic.image.loader import ImageLoader
from relic.matching.fetcher import ImageFetcher
from relic.matching.geometry import orb_similarity
from relic.matching.scorer import MatchScore, combined_score, phash_similarity


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
    ) -> MatchScore:
        candidate_path = self.fetcher.fetch(
            candidate_url,
            destination,
        )

        candidate = self.loader.load(candidate_path)

        phash_score = phash_similarity(
            source.phash,
            candidate.phash,
        )

        geometric_match = orb_similarity(
            source.path,
            candidate.path,
        )

        return combined_score(phash_score, geometric_match)