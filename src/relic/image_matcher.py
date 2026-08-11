from relic.image import Image
from relic.similarity import hamming_distance, parse_phash, similarity


def match(first: Image, second: Image) -> float:
    first_hash = parse_phash(first.phash)
    second_hash = parse_phash(second.phash)

    distance = hamming_distance(first_hash, second_hash)

    return similarity(first_hash, second_hash, 64)