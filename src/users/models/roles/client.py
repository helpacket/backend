"""Client model definitions."""

import logging

from django.db.models import (
    OneToOneField,
    CASCADE,
)

from .abc import Role

logger = logging.getLogger(__name__)


# TODO: Rename to Client


class Client(Role):
    """Client model."""

    party = OneToOneField("users.Party", related_name="client", on_delete=CASCADE, primary_key=True)
