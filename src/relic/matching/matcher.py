from relic.image import Image
from relic.matching.scorer import phash_similarity


def match(first: Image, second: Image) -> float:
    return phash_similarity(
        first.phash,
        second.phash,
    )