"""Definition of Supply model."""

import logging

from django.db.models import (
    ForeignKey,
    CASCADE,
    SET_NULL,
)

from .abc import (
    Operation
)

logger = logging.getLogger(__name__)


class Supply(Operation):
    """Supply model."""

    supplier = ForeignKey('users.Supplier', related_name='supplies', on_delete=CASCADE)

    product = ForeignKey('products.Product', related_name='supplies', on_delete=CASCADE)

    transaction = ForeignKey(
        'transactions.Transaction', related_name='supplies', null=True, blank=True, on_delete=SET_NULL,
    )
