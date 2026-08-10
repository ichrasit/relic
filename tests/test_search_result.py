from datetime import datetime

from relic.search_result import SearchResult


def test_search_result_extracts_domain():
    result = SearchResult(
        url="https://example.com/images/photo.jpg",
        title="Example photo",
        source="example",
        discovered_at=datetime.now(),
        match_score=0.98,
    )

    assert result.domain == "example.com"

def test_high_match_score_is_match():
    result = SearchResult(
        url="https://example.com/photo.jpg",
        title="Example",
        source="example",
        discovered_at=datetime.now(),
        match_score=0.95,
    )

    assert result.is_match is True