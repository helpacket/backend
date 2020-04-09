import logging

from graphene import (
    relay,
    ObjectType,
    Field, String, ID)
from graphene_django.filter import (
    DjangoFilterConnectionField,
)
from graphene_django.types import (
    DjangoObjectType,
)

from graphql_relay import (
    from_global_id,
)

from core.models import (
    Concert,
    Band,
)

logger = logging.getLogger(__name__)


class ConcertNode(DjangoObjectType):
    class Meta:
        model = Concert
        filter_fields = ['id']
        interfaces = (relay.Node,)


class BandNode(DjangoObjectType):
    class Meta:
        model = Band
        filter_fields = ['id', 'name', 'creation_datetime']
        interfaces = (relay.Node,)


class BandMutation(relay.ClientIDMutation):
    class Input:
        id = ID()
        name = String()
        description = String()
        image_url = String()

    result = Field(BandNode)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **kwargs):
        identifier = kwargs.pop("id", None)
        if identifier is not None:
            identifier = from_global_id(identifier)[1]
        result, _ = Band.objects.update_or_create(defaults=kwargs, pk=identifier)
        return cls(result=result)


class Query(ObjectType):
    concerts = DjangoFilterConnectionField(ConcertNode)
    bands = DjangoFilterConnectionField(BandNode)


class Mutation(ObjectType):
    band = BandMutation.Field()
