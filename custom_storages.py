"""This file is used to set up the custom storage for the static files."""
from django.conf import settings
from storages.backends.s3boto3 import S3Boto3Storage


class StaticStorage(S3Boto3Storage):
    """This class is used to set up the custom storage for the static files."""

    location = settings.STATICFILES_LOCATION


class MediaStorage(S3Boto3Storage):
    """This class is used to set up the custom storage for the media files."""

    location = settings.MEDIAFILES_LOCATION
