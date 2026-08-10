def similarity(distance: int, hash_size: int = 64) -> float:
    if distance <= 0:
        raise ValueError("Distance cannot be negative")

    if distance > hash_size:
        raise ValueError("Distance cannot exceed hash size")

    if distance < 0:
        raise ValueError("Distance cannot be negative")
    return 1.0 - (distance / hash_size)
