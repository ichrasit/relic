from dataclasses import dataclass
from datetime import datetime
from urllib.parse import urlparse

from relic.matching.scorer import MatchScore

MATCH_THRESHOLD = 0.85


@dataclass(frozen=True)
class SearchResult:
    url: str
    title: str
    source: str
    discovered_at: datetime
    match_score: MatchScore

    @property
    def domain(self) -> str:
        return urlparse(self.url).netloc

    @property
    def is_match(self) -> bool:
        return self.match_score.combined_score >= MATCH_THRESHOLD