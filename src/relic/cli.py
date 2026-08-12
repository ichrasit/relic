import argparse
from pathlib import Path

from relic.application import RelicApplication


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="relic",
        description="Visual OSINT investigation tool",
    )

    parser.add_argument(
        "image",
        type=Path,
        help="Path to the image to investigate",
    )
    return parser

def run(
        applicaton: RelicApplication,
        image_path: Path,
) -> int:
        results = applicaton.investigate(image_path)

        for result in results:
              print(f"[{results.match_score:2.f}] {result.title}")
              print(f"  {result.url}")
              print(f". {result.domain}")
              print()

        return 0

def main() -> int:
      parser = build_parser()
      args = parser.parse_args()

      raise RuntimeError(
            "CLI dependencies are not configured yet"
      )

if __name__ == "__main__":
      raise SystemExit(main())
