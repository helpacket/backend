import graphene
from graphene_django.types import DjangoObjectType
from core.models import Concert, Bar, Band
from datetime import datetime


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
        return Concert.objects.filter(start_datetime__date__gte=datetime.now().date()).order_by('start_datetime')

    def resolve_concert(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return Concert.objects.get(pk=id)

        return None
