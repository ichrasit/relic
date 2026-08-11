from relic.serpapi_provider import SerpApiProvider

class FakeResponse:
    def raise_for_status(self):
        pass
    def json(self):
        return{
            "visual_matches": [],
        }


class FakeClient:

    def __init__(self):
        self.url = None
        self.params = None

    def get(self, url, params):
        self.url = url
        self.params = params

        return FakeResponse()


def test_serpapi_provider_builds_request(monkeypatch):
    monkeypatch.setenv("SERPAPI_API_KEY", "test-key")

    client = FakeClient()
    provider = SerpApiProvider(client=client)

    results = provider.search(
        "https://example.com/photo.jpg"
    )

    assert results == []
    assert client.url == "https://serpapi.com/search.json"

    assert client.params == {
        "engine":"google_lens",
        "url": "https://example.com/photo.jpg",
        "type": "all",
        "api_key": "test-key",
    }

