from graphene import (
    Schema,
    ObjectType,
)

from .types import (
    Query as QuerySchema,
)


class Query(QuerySchema, ObjectType):
    pass


schema = Schema(query=Query)
