from relic.similarity import similarity

def test_idential_hashes_have_full_similarity():
    assert similarity(0) == 1.0

def test_half_distance_has_half_similarity():
    assert similarity(32) == 0.5

def test_maximum_distance_has_zero_similarity():
    assert similarity(64) == 0.0