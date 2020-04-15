"""Definition of Product model."""

import logging

from django.db import models

logger = logging.getLogger(__name__)


class Product(models.Model):
    """Product model."""

    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
