from dataclasses import dataclass
from relic.search_result import SearchResult

@dataclass(frozen=True)
class InvestigationResult:
    image_url:str
    results: list[SearchResult]