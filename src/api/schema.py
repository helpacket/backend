from graphene import (
    Schema,
)

from .types import (
    Query,
    Mutation,
)

schema = Schema(
    query=Query,
    mutation=Mutation,
)
