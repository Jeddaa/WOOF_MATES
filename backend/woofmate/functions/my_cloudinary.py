"""
Contains the necessary setup to upload an image
to cloudinary in order to store the image url
"""

from woofmate.config import settings
import cloudinary
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from fastapi import File, UploadFile
from typing import Annotated, Optional
import logging

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET_KEY,
    secure=True
)


async def upload_image_to_cloudinary(
    foldername: str, file: Annotated[bytes, File()],
    username: str, field_name: str,
) -> Optional[str]:
    """
    Uploads an image to Cloudinary and returns the public URL.
    Returns None if there was an error uploading the image.
    """
    try:
        result = upload(
            file,
            public_id=f'{foldername}/{username}_{field_name}'
        )
        url, options = cloudinary_url(
            result['public_id'],
            format=result['format'],
            crop="fill"
        )
        return url
    except Exception as e:
        logging.exception("Cloudinary_Error: %s", str(e))
        return None
