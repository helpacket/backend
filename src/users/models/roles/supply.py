"""SupplyRole model definitions."""

import logging

from django.db.models import (
    OneToOneField,
    CASCADE,
)

from .abc import (
    Role,
)

logger = logging.getLogger(__name__)


class SupplyRole(Role):
    """SupplyRole model."""

    party = OneToOneField("users.Party", on_delete=CASCADE, primary_key=True)
