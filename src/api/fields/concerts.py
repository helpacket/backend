import logging

from graphene.relay import (
    Node,
)
from graphene_django.types import (
    DjangoObjectType,
)

from core.models import (
    Concert,
)

logger = logging.getLogger(__name__)


class ConcertNode(DjangoObjectType):
    class Meta:
        model = Concert
        filter_fields = ['id']
        interfaces = (Node,)
