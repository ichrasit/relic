def hamming_distance(left: int, right: int) -> int:
    return (left ^ right).bit_count()


def similarity(left: int, right: int, hash_size: int) -> float:
    if hash_size <= 0:
        raise ValueError("hash_size must be positive")

    distance = hamming_distance(left, right)

    if distance > hash_size:
        raise ValueError("hamming distance cannot exceed hash size")

    return 1.0 - (distance / hash_size)


def parse_phash(value: str) -> int:
    return int(value, 16)