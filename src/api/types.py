from graphene import relay
from graphene_django.filter import (
    DjangoFilterConnectionField,
)
from graphene_django.types import (
    DjangoObjectType,
)

from core.models import (
    Concert,
    Band,
)


class ConcertNode(DjangoObjectType):
    class Meta:
        model = Concert
        filter_fields = ['id']
        interfaces = (relay.Node,)


class BandNode(DjangoObjectType):
    class Meta:
        model = Band
        filter_fields = ['id']
        interfaces = (relay.Node,)


class Query(object):
    concert = relay.Node.Field(ConcertNode)
    all_concerts = DjangoFilterConnectionField(ConcertNode)

    band = relay.Node.Field(BandNode)
    all_bands = DjangoFilterConnectionField(BandNode)
