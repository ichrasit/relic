from dataclasses import dataclass

from relic.matching.geometry import GeometricMatch

PHASH_WEIGHT = 0.4
GEOMETRIC_WEIGHT = 0.6


@dataclass(frozen=True)
class MatchScore:
    phash_score: float
    geometric_score: float
    good_matches: int
    combined_score: float


def hamming_distance(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def parse_phash(value: str) -> int:
    return int(value, 16)


def phash_similarity(
    left: str,
    right: str,
    hash_size: int = 64,
) -> float:
    if hash_size <= 0:
        raise ValueError("hash_size must be positive")

    left_hash = parse_phash(left)
    right_hash = parse_phash(right)

    distance = hamming_distance(left_hash, right_hash)

    if distance > hash_size:
        raise ValueError("hamming distance cannot exceed hash size")

    return 1.0 - (distance / hash_size)


def combined_score(
    phash_score: float,
    geometric_match: GeometricMatch,
    phash_weight: float = PHASH_WEIGHT,
    geometric_weight: float = GEOMETRIC_WEIGHT,
) -> MatchScore:
    if not (0.0 <= phash_score <= 1.0):
        raise ValueError("phash_score must be between 0 and 1")

    total_weight = phash_weight + geometric_weight

    if total_weight <= 0:
        raise ValueError("weights must sum to a positive value")

    combined = (
        phash_score * phash_weight
        + geometric_match.score * geometric_weight
    ) / total_weight

    return MatchScore(
        phash_score=phash_score,
        geometric_score=geometric_match.score,
        good_matches=geometric_match.good_matches,
        combined_score=combined,
    )