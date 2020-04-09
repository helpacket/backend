from graphene import (
    Schema,
    ObjectType,
)
from graphene_django.filter import (
    DjangoFilterConnectionField,
)
from .fields import (
    BandMutation,
    BandNode,
    ConcertNode,
)


class Query(ObjectType):
    concerts = DjangoFilterConnectionField(ConcertNode)
    bands = DjangoFilterConnectionField(BandNode)


class Mutation(ObjectType):
    band = BandMutation.Field()


schema = Schema(
    query=Query,
    mutation=Mutation,
)
