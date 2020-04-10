from django.contrib.admin import (
    register,
    ModelAdmin,
)

from ...models import (
    SupplyRole,
)


@register(SupplyRole)
class SupplyRoleAdmin(ModelAdmin):
    list_display = ('party',)
