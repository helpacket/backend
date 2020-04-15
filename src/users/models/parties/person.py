"""Person model definitions."""

import logging

from django.contrib.auth.models import AbstractUser
from .abc import Party

logger = logging.getLogger(__name__)


class Person(AbstractUser, Party):
    """Person model.

    This is the user model representation.
    """

    pass
