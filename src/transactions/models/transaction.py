"""Definition of Transition model."""

import logging

from django.db.models import (
    Model,
    AutoField,
    DateTimeField,
    OneToOneField,
    CASCADE,
)

logger = logging.getLogger(__name__)


class Transaction(Model):
    """Transition model."""

    id = AutoField(primary_key=True)

    creation_datetime = DateTimeField(auto_now_add=True)

    last_modification_datetime = DateTimeField(auto_now=True)

    request = OneToOneField("transactions.Request", on_delete=CASCADE)
