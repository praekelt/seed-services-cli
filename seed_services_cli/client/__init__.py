"""Seed Services client library."""

from .identity_store import IdentityStoreApiClient
from .stage_based_messaging import StageBasedMessagingApiClient

__version__ = "0.0.2"

__all__ = [
    'IdentityStoreApiClient', 'StageBasedMessagingApiClient'
]
