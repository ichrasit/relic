import httpx

from relic.image import Image

class CloudinaryUploader:
    def __init__(
            self,
            cloud_name: str,
            upload_preset: str,
            client: httpx.Client | None = None,
    ):
        self.cloud_name = cloud_name
        self.upload_preset = upload_preset
        self.client = client or httpx.Client(timeout=30.0)

    def upload(self, image: Image) -> str:
        url = (
            f"https://api.cloudinary.com/v1_1"
            f"{self.cloud_name}/image/upload"
        )

        with image.path.open("rb") as file:
            response = self.client.post(
                url,
                data={"upload_preset": self.upload_preset},
                files={"file": file},
            )

            response.raise_for_status()
            return response.json()["secure_url"]