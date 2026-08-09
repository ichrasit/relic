from pathlib import Path
from relic.filesystem import file_exists

def test_file_exists_for_existing_file(tmp_path):
    file_path = tmp_path / "photo.jpg"
    file_path.touch()

    assert file_exists(file_path)

def test_file_exists_for_missing_file(tmp_path):
    file_path = tmp_path / "missing.jpg"
    assert not file_exists(file_path)

def test_file_exists_for_directoru(tmp_path):
    directory = tmp_path / "photos"
    directory.mkdir()

    assert not file_exists(directory)