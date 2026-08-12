from relic.search.result import SearchResult


def rank(results: list[SearchResult]) -> list[SearchResult]:
    return sorted(
        results,
        key=lambda result: result.match_score.combined_score,
        reverse=True,
    )