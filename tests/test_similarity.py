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