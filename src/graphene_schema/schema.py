import graphene

from .types import Query as SchemaQuery


class Query (SchemaQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
