"""Definition of API endpoints."""

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
from transactions.api.supply import SupplyMutation
from users.api import (
    PersonNode,
)
from transactions.api import (
    SupplyNode,
    RequestNode,
    RequestMutation,
)
from products.api import (
    ProductNode,
)


class Query(ObjectType):
    """Accessible GraphQL queries."""

    concerts = DjangoFilterConnectionField(ConcertNode)
    bands = DjangoFilterConnectionField(BandNode)
    people = DjangoFilterConnectionField(PersonNode)
    supplies = DjangoFilterConnectionField(SupplyNode)
    requests = DjangoFilterConnectionField(RequestNode)
    products = DjangoFilterConnectionField(ProductNode)


class Mutation(ObjectType):
    """Accessible GraphQL mutations."""

    token_auth = ObtainJSONWebToken.Field()
    verify_token = Verify.Field()
    refresh_token = Refresh.Field()

    band = BandMutation.Field()
    request = RequestMutation.Field()
    supply = SupplyMutation.Field()


schema = Schema(
    query=Query,
    mutation=Mutation,
)
