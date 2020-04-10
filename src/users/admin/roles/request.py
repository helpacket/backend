from django.contrib.admin import (
    register,
    ModelAdmin,
)

from ...models import (
    RequestRole,
)


@register(RequestRole)
class RequestRoleAdmin(ModelAdmin):
    list_display = ('party',)
