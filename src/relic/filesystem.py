from pathlib import Path

def file_exists(path: Path) -> bool:
    return path.is_file()