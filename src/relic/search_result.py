from dataclasses import dataclass
from datetime import datetime
from urllib.parse import urlparse

@dataclass(frozen=True)
class SearchResult:
    url:str
    title:str
    source:str
    discovered_at:datetime
    match_score:float

    @property
    def domain(self) -> str:
        return urlparse(self.url).netloc
    