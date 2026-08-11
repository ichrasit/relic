from relic.image import Image
from relic.similarity import parse_phash, similarity


PHASH_SIZE = 64


def match(first: Image, second: Image) -> float:
    first_hash = parse_phash(first.phash)
    second_hash = parse_phash(second.phash)

    return similarity(
        first_hash,
        second_hash,
        hash_size=PHASH_SIZE,
    )