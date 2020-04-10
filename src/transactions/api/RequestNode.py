import logging
from graphql_jwt.decorators import login_required
from graphene.relay import Node
from graphene_django.types import DjangoObjectType
from ..models import Request


logger = logging.getLogger(__name__)


class RequestNode(DjangoObjectType):
    class Meta:
        model = Request
        fields = ("amount", "creation_datetime", "product", "status", )
        filter_fields = ()
        interfaces = (Node,)

    # @classmethod
    # @login_required
    # def get_queryset(cls, queryset, info):
    #     user = info.context.user
    #     return queryset.filter(username=user.username)
