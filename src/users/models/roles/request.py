"""RequestRole model definitions."""

import logging

from django.db.models import (
    OneToOneField,
    CASCADE,
)

from .abc import (
    Role,
)
logger = logging.getLogger(__name__)


class RequestRole(Role):
    """RequestRole model."""

    party = OneToOneField("users.Party", on_delete=CASCADE, primary_key=True)
