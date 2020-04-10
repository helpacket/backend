from graphene import (
    Schema,
    ObjectType,
)
from graphql_jwt import (
    ObtainJSONWebToken,
    Verify,
    Refresh,
)

from graphene_django.filter import (
    DjangoFilterConnectionField,
)

from core.api import (
    BandMutation,
    BandNode,
    ConcertNode,
)
from parties.api import (
    PersonNode,
)
from transactions.api import (
    SupplyNode,
    RequestNode,
)
from products.api import (
    ProductNode,
)


class Query(ObjectType):
    concerts = DjangoFilterConnectionField(ConcertNode)
    bands = DjangoFilterConnectionField(BandNode)
    people = DjangoFilterConnectionField(PersonNode)
    supplies = DjangoFilterConnectionField(SupplyNode)
    requests = DjangoFilterConnectionField(RequestNode)
    products = DjangoFilterConnectionField(ProductNode)


class Mutation(ObjectType):
    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()

    band = BandMutation.Field()


schema = Schema(
    query=Query,
    mutation=Mutation,
)
