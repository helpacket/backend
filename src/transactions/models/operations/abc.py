"""Definition of Operation model."""

from abc import abstractmethod

from django.db.models import (
    Model,
    AutoField,
    DateTimeField,
    IntegerField,
)

from products.models import Product  # TODO: Locate under "TYPE_CHECKING".


class Operation(Model):
    """Operation model."""

    class Meta:
        abstract = True

    PENDING = 0
    ASSIGNED = 1
    SENT = 2
    STATUS_CHOICES = (
        (PENDING, "pending"),
        (ASSIGNED, "assigned"),
        (SENT, "sent"),
    )

    id = AutoField(primary_key=True)

    creation_datetime = DateTimeField(auto_now_add=True)

    last_modification_datetime = DateTimeField(auto_now=True)

    amount = IntegerField()

    status = IntegerField(choices=STATUS_CHOICES, default=PENDING)

    @property
    @abstractmethod
    def product(self) -> Product:
        """Product attribute.

        :return: A product object.
        """
        pass
