from datetime import (
    datetime,
)

import graphene
from graphene_django.types import (
    DjangoObjectType,
)

from core.models import (
    Concert,
    Bar,
    Band,
)


class ConcertType(DjangoObjectType):
    class Meta:
        model = Concert


class BarType(DjangoObjectType):
    class Meta:
        model = Bar


class BandType(DjangoObjectType):
    class Meta:
        model = Band


class Query(object):
    concert = graphene.Field(
        # ConcertType, id=graphene.Int(), band=graphene.String(), description=graphene.String(),
        ConcertType, id=graphene.Int()
    )

    all_concerts = graphene.List(ConcertType)

    def resolve_all_concerts(self, info, **kwargs):
        query = Concert.objects.filter(
            start_datetime__date__gte=datetime.now().date()
        )
        query = query.order_by('start_datetime')
        return query

    def resolve_concert(self, id, **kwargs):
        identifier = id

        if identifier is not None:
            return Concert.objects.get(pk=identifier)

        return None
