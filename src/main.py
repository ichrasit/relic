import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from relic.application import RelicApplication
from relic.cloudinary_uploader import CloudinaryUploader
from relic.investigation.investigator import Investigator
from relic.search.serpapi import SerpApiProvider

load_dotenv()


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: relic <image>")
        return 1

    image_path = Path(sys.argv[1])

    if not image_path.is_file():
        print(f"Error: image not found {image_path}")
        return 1
    
    cloud_name = os.getenv("CLOUDINARY_CLOUD_NAME")
    upload_preset = os.getenv("CLOUDINARY_UPLOAD_PRESET")

    if not cloud_name or not upload_preset:
        print(
            "Error: CLOUDINARY_CLOUD_NAME and" \
            "CLOUDINARY_UPLOAD_PRESET must be set"
        )
        return 1

    uploader = CloudinaryUploader(
        cloud_name=cloud_name,
        upload_preset=upload_preset,
    )
    provider = SerpApiProvider()

    investigator = Investigator(
        provider=provider,
        uploader=uploader,
    )

    application = RelicApplication(investigator)

    try:
        results = application.investigate(image_path)
    except Exception as exc:
        print(f"Investigation failed: {exc}")
        return 1

    if not results:
        print("No results found.")

    print(f"Found {len(results)} results:\n")

    for result in results:
        print(f"[{result.match_score:.2f}] {result.title}")
        print(f"  {result.url}")
        print(f"  {result.domain}")
        print()

    return 0


if __name__ == "__main__":
    raise SystemExit(main())