from pathlib import Path

from relic.image import Image
from relic.matching.matcher import ImageMatcher
from relic.matching.ranking import rank
from relic.search.result import SearchResult


class MatchingPipeline:
    def __init__(
        self,
        matcher: ImageMatcher | None = None,
    ):
        self.matcher = matcher or ImageMatcher()

    def process(
        self,
        source: Image,
        results: list[SearchResult],
        workspace: Path,
    ) -> list[SearchResult]:
        matched_results = []

        for index, result in enumerate(results):
            destination = workspace / f"candidate_{index}.jpg"

            try:
                score = self.matcher.match(
                    source,
                    result.url,
                    destination,
                )
            except Exception:
                continue

            matched_results.append(
                SearchResult(
                    url=result.url,
                    title=result.title,
                    source=result.source,
                    discovered_at=result.discovered_at,
                    match_score=score,
                )
            )

        return rank(matched_results)