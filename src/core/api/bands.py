import logging

from graphene import (
    Field,
    String,
    ID,
    Boolean,
)
from graphene.relay import (
    Node,
    ClientIDMutation,
)
from graphene_django.types import (
    DjangoObjectType,
)

from graphql_jwt.decorators import (
    login_required,
)
from graphql_relay import (
    from_global_id,
)

from ..models import (
    Band,
)

logger = logging.getLogger(__name__)


class BandNode(DjangoObjectType):
    class Meta:
        model = Band
        filter_fields = ['id', 'name', 'creation_datetime']
        interfaces = (Node,)

    @classmethod
    @login_required
    def get_queryset(cls, queryset, info):
        return queryset


class BandMutation(ClientIDMutation):
    class Input:
        id = ID()

        name = String()
        description = String()
        image_url = String()

        delete = Boolean(default=False)

    result = Field(BandNode)
    ok = Boolean()

    @classmethod
    @login_required
    def mutate_and_get_payload(cls, root, info, **kwargs):

        identifier = kwargs.pop("id", None)
        if identifier is not None:
            identifier = from_global_id(identifier)[1]

        if kwargs.pop("delete", False):
            result = Band.objects.get(pk=identifier)
            result.delete()
            return cls(ok=True)

        user = info.context.user
        kwargs["owner"] = user

        result, _ = Band.objects.update_or_create(defaults=kwargs, pk=identifier)
        return cls(result=result, ok=True)
