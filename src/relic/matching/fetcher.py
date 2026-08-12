from pathlib import Path

import httpx


class ImageFetcher:
    def __init__(
        self,
        client: httpx.Client | None = None,
    ):
        self.client = client or httpx.Client(
            timeout=15.0,
            follow_redirects=True,
        )

    def fetch(self, url: str, destination: Path) -> Path:
        response = self.client.get(url)
        response.raise_for_status()

        destination.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        destination.write_bytes(response.content)

        return destination