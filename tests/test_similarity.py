from relic.similarity import similarity

def test_idential_hashes_have_full_similarity():
    assert similarity(0) == 1.0