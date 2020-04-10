from django.contrib.admin import (
    register,
    ModelAdmin,
)

from ...models import (
    Client,
)


@register(Client)
class ClientAdmin(ModelAdmin):
    list_display = ('party',)
