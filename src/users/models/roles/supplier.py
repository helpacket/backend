"""Supplier model definitions."""

import logging

from django.db.models import (
    OneToOneField,
    CASCADE,
)

from .abc import Role

logger = logging.getLogger(__name__)


# TODO: Rename to Supplier


class Supplier(Role):
    """Supplier model."""

    party = OneToOneField("users.Party", related_name="supplier", on_delete=CASCADE, primary_key=True)
