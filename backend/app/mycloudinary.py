"""
Contains the necessary setup to upload an image
to cloudinary in order to store the image url
"""

from app.config import settings
from cloudinary.uploader import upload
from cloudinary.utils import cloudinary_url
from fastapi import File, UploadFile
from typing import Optional
import logging

cloudinary.config(
    cloud_name=settings.CLOUDINARY_CLOUD_NAME,
    api_key=settings.CLOUDINARY_API_KEY,
    api_secret=settings.CLOUDINARY_API_SECRET_KEY,
    secure=True
)


def upload_image_to_cloudinary(file: UploadFile) -> Optional[str]:
    """
    Uploads an image to Cloudinary and returns the public URL.
    Returns None if there was an error uploading the image.
    """
    try:
        result = upload(file.file)
        url, options = cloudinary_url(
            result['public_id'],
            format=result['format'],
            crop="fill"
        )
        return url
    except Exception as e:
        logging.exception("Error: %s", str(e))
        return None
