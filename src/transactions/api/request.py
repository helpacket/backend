import logging

from graphene import Int, ID, ClientIDMutation, Field, Boolean
from graphql_jwt.decorators import (
    login_required,
)
from graphene.relay import (
    Node,
)
from graphene_django.types import (
    DjangoObjectType,
)
from graphql_relay import from_global_id

from users.models import Client
from ..models import (
    Request,
)


logger = logging.getLogger(__name__)


class RequestNode(DjangoObjectType):
    class Meta:
        model = Request
        fields = ("amount", "creation_datetime", "product", "status", )
        filter_fields = ()
        interfaces = (Node,)

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        user = info.context.user
        return queryset.filter(requester__party=user)


class RequestMutation(ClientIDMutation):
    class Input:
        id = ID()

        amount = Int()
        product_id = ID()

    result = Field(RequestNode)
    ok = Boolean()

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **kwargs):

        identifier = kwargs.pop("id", None)
        if identifier is not None:
            identifier = from_global_id(identifier)[1]

        if kwargs.pop("delete", False):
            result = Request.objects.get(pk=identifier)
            result.delete()
            return cls(ok=True)

        product_id = kwargs.pop("product_id", None)
        if product_id is not None:
            product_id = from_global_id(product_id)[1]
        kwargs["product_id"] = product_id

        user = info.context.user
        kwargs["client_id"] = user.id

        _, _ = Client.objects.get_or_create(pk=user.id)

        result, _ = Request.objects.update_or_create(defaults=kwargs, pk=identifier)
        return cls(result=result, ok=True)
