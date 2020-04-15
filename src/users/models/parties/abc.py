"""Party model definitions."""

import logging

from django.db.models import (
    Model,
    AutoField,
)

logger = logging.getLogger(__name__)


class Party(Model):
    """Party model."""

    id = AutoField(primary_key=True)

    @property
    def is_supplier(self) -> bool:
        """Flag to now if the party is a Supplier.

        :return: A boolean value.
        """
        return hasattr(self, "supplier")

    @property
    def is_client(self) -> bool:
        """Flag to now if the party is a Client.

        :return: A boolean value.
        """
        return hasattr(self, "client")
