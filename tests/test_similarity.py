import pytest

from relic.similarity import similarity


def test_identical_hashes_have_full_similarity():
    assert similarity(0x00, 0x00, hash_size=64) == 1.0


def test_half_distance_has_half_similarity():
    assert similarity(0x00000000, 0xFFFFFFFF, hash_size=64) == 0.5


def test_maximum_distance_has_zero_similarity():
    assert similarity(0x0000000000000000, 0xFFFFFFFFFFFFFFFF, hash_size=64) == 0.0


def test_similarity_rejects_non_positive_hash_size():
    with pytest.raises(ValueError, match="hash_size must be positive"):
        similarity(0, 0, hash_size=0)


def test_similarity_rejects_distance_above_hash_size():
    with pytest.raises(ValueError, match="cannot exceed hash size"):
        similarity(0, 0x1FF, hash_size=8)