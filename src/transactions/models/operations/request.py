"""Definition of Request model."""

import logging

from django.db.models import (
    CASCADE,
    ForeignKey,
)

from .abc import (
    Operation,
)

logger = logging.getLogger(__name__)


class Request(Operation):
    """Request model."""

    requester = ForeignKey('users.RequestRole', related_name='requests', on_delete=CASCADE)

    product = ForeignKey('products.Product', related_name='requests', on_delete=CASCADE)
