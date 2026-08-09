from pathlib import Path

from relic.fingerprint import sha256


def test_sha256_returns_known_hash(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("hello relic!")

    assert sha256(file_path) == (
        "ee95a5035fe436dc9b42fdf64a7c651d24c80edc4fe721bf537391615a8c43e9"
    )

def test_sha256_is_deterministic(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("relic")

    first = sha256(file_path)
    second = sha256(file_path)

    assert first == second


def test_sha256_changes_when_file_changes(tmp_path):
    file_path = tmp_path / "test.txt"
    file_path.write_text("relic")
    first = sha256(file_path)

    file_path.write_text("relic osint")
    second = sha256(file_path)

    assert first != second


def test_sha256_empty_file(tmp_path):
    file_path = tmp_path / "empty"

    file_path.touch()

    assert sha256(file_path) == (
        "e3b0c44298fc1c149afbf4c8996fb924"
        "27ae41e4649b934ca495991b7852b855"
    )