import argparse
from pathlib import Path


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


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    print(f"Investigation target: {args.image}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())