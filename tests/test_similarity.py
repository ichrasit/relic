from relic.similarity import similarity
import pytest

def test_idential_hashes_have_full_similarity():
    assert similarity(0) == 1.0

def test_half_distance_has_half_similarity():
    assert similarity(32) == 0.5

def test_maximum_distance_has_zero_similarity():
    assert similarity(64) == 0.0

def test_similarity_rejects_negative_distance():
    with pytest.raises(ValueError, match="cannot be negative"):
        similarity(-1)

def test_similarity_rejects_distance_above_hash_size():
    with pytest.raises(ValueError, match="cannot exceed hash size"):
        similarity(65)

def test_similarity_supports_custom_hash_size():
    assert similarity(8, hash_size=16) == 0.5

@pytest.mark.parametrize(
    ("distance", "expected"),
    [
        (0, 1.0),
        (16, 0.75),
        (32, 0.5),
        (48, 0.25),
        (64, 0.0),
    ],
)
def test_similarity_returns_expected_values(distance, expected):
    assert similarity(distance) == expected

def test_similarity_rejects_non_positive_hash_size():
    with pytest.raises(ValueError, match="hash size"):
        similarity(0, hash_size=0)