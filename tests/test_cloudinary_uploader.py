from pathlib import Path

from relic.cloudinary_uploader import CloudinaryUploader
from relic.image import Image
from relic.image_metadata import ImageMetaData


class FakeResponse:
    def raise_for_status(self):
        pass

    def json(self):
        return {
            "secure_url": "https://res.cloudinary.com/test/image/upload/photo.jpg"
        }


class FakeClient:
    def __init__(self):
        self.url = None
        self.data = None
        self.files = None

    def post(self, url, data, files):
        self.url = url
        self.data = data
        self.files = files
        return FakeResponse()


def test_cloudinary_uploader_uploads_image(tmp_path):
    image_path = tmp_path / "photo.jpg"
    image_path.write_bytes(b"fake image")

    image = Image(
        path=image_path,
        metadata=ImageMetaData(
            width=100,
            height=100,
            format="JPEG",
            mode="RGB",
        ),
        sha256="abc",
        phash="0000000000000000",
    )

    client = FakeClient()

    uploader = CloudinaryUploader(
        cloud_name="test-cloud",
        upload_preset="relic_uploads",
        client=client,
    )

    result = uploader.upload(image)

    assert result == (
        "https://res.cloudinary.com/test/image/upload/photo.jpg"
    )

    assert client.url == (
        "https://api.cloudinary.com/v1_1/test-cloud/image/upload"
    )

    assert client.data == {
        "upload_preset": "relic_uploads",
    }