from pathlib import Path
from PIL import Image as PILImage

def file_exists(path: Path) -> bool:
    return path.is_file()



def is_image(path: Path) -> bool:
    if not path.is_file():
        return False
    
    try:
        with PILImage.open(path) as image:
            image.verify()
        
    except (OSError, SyntaxError):
        return False
    
    return True