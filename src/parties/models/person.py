"""Set of person related models."""

from django.contrib.auth.models import (
    AbstractUser,
)


class Person(AbstractUser):
    """Person model.

    This is the user model representation.
    """
    pass
