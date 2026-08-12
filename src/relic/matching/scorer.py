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