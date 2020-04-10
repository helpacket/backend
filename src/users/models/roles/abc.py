"""Role model definitions."""

import logging
from abc import abstractmethod

from django.db.models import (
    Model,
    DateTimeField,
)

from ...models import Party  # TODO: Locate under "TYPE_CHECKING".

logger = logging.getLogger(__name__)


class Role(Model):
    """Role model."""

    class Meta:
        abstract = True

    creation_datetime = DateTimeField(auto_now_add=True)

    last_modification_datetime = DateTimeField(auto_now=True)

    @property
    @abstractmethod
    def party(self) -> Party:
        """party attribute.

        :return:A party object.
        """
        pass
