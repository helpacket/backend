"""Party model definitions."""

import logging

from django.db.models import (
    Model,
)

logger = logging.getLogger(__name__)


class Party(Model):
    """Party model."""

    @property
    def is_supplier(self) -> bool:
        return hasattr(self, "supplier")

    @property
    def is_client(self) -> bool:
        return hasattr(self, "client")
