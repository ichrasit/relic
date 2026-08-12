import os

def get_required_env(name: str) -> str:
    value = os.getenv(name)

    if not value:
        raise RuntimeError(f"{name} is not set")
    return value


def get_serp_api_key() -> str:
    return get_required_env("SERPAPI_API_KEY")

def get_cloudinary_cloud_name() -> str:
    return get_required_env ("CLOUDINARY_CLOUD_NAME")

def get_cloudinary_upload_preset() -> str:
    return get_required_env("CLOUDINARY_UPLOAD_PRESET")

