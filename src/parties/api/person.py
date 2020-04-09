import logging

from graphql_jwt.decorators import (
    login_required,
)
from graphene.relay import (
    Node,
)
from graphene_django.types import (
    DjangoObjectType,
)

from ..models import (
    Person,
)

logger = logging.getLogger(__name__)


class PersonNode(DjangoObjectType):
    class Meta:
        model = Person
        fields = ("username", "email", "first_name", "last_name")
        filter_fields = ['username', 'email']
        interfaces = (Node,)

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        user = info.context.user
        return queryset.filter(username=user.username)
