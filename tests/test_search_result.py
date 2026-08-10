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