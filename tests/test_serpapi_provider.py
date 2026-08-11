from relic.serpapi_provider import SerpApiProvider


class FakeResponse:

    def __init__(self, data):
        self.data = data

    def raise_for_status(self):
        pass

    def json(self):
        return self.data


class FakeClient:

    def __init__(self, response):
        self.response = response
        self.url = None
        self.params = None

    def get(self, url, params):
        self.url = url
        self.params = params

        return FakeResponse(self.response)


def test_serpapi_provider_builds_request(monkeypatch):
    monkeypatch.setenv("SERPAPI_API_KEY", "test-key")

    client = FakeClient({
        "visual_matches": [],
    })

    provider = SerpApiProvider(client=client)

    results = provider.search(
        "https://example.com/photo.jpg"
    )

    assert results == []

    assert client.url == "https://serpapi.com/search.json"

    assert client.params == {
        "engine": "google_lens",
        "url": "https://example.com/photo.jpg",
        "type": "all",
        "api_key": "test-key",
    }


def test_serpapi_provider_parses_visual_match(monkeypatch):
    monkeypatch.setenv("SERPAPI_API_KEY", "test-key")

    client = FakeClient({
        "visual_matches": [
            {
                "link": "https://example.com/photo.jpg",
                "title": "Example photo",
                "source": "Example",
            }
        ]
    })

    provider = SerpApiProvider(client=client)

    results = provider.search(
        "https://example.com/photo.jpg"
    )

    assert len(results) == 1
    assert results[0].url == "https://example.com/photo.jpg"
    assert results[0].title == "Example photo"
    assert results[0].source == "Example"


def test_serpapi_provider_skips_match_without_link(monkeypatch):
    monkeypatch.setenv("SERPAPI_API_KEY", "test-key")

    client = FakeClient({
        "visual_matches": [
            {
                "title": "Broken result",
                "source": "Example",
            },
            {
                "link": "https://example.com/photo.jpg",
                "title": "Valid result",
                "source": "Example",
            },
        ]
    })

    provider = SerpApiProvider(client=client)

    results = provider.search(
        "https://example.com/photo.jpg"
    )

    assert len(results) == 1
    assert results[0].url == "https://example.com/photo.jpg"