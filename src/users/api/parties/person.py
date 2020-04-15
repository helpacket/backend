"""PersonNode endpoint implementation."""

import logging

from graphene import Boolean
from graphql_jwt.decorators import login_required
from graphene.relay import Node
from graphene_django.types import DjangoObjectType

from ...models import Person

logger = logging.getLogger(__name__)


class PersonNode(DjangoObjectType):
    """PersonNode endpoint."""

    is_client = Boolean()
    is_supplier = Boolean()

    class Meta:
        """Meta class."""

        model = Person
        fields = ("username", "email", "first_name", "last_name")
        filter_fields = (
            "username",
            "email",
        )
        interfaces = (Node,)

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        """Provide the queryset."""
        user = info.context.user
        return queryset.filter(username=user.username)
