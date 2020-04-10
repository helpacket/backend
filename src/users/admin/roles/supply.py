from django.contrib.admin import (
    register,
    ModelAdmin,
)

from ...models import (
    Supplier,
)


@register(Supplier)
class SupplierAdmin(ModelAdmin):
    list_display = ('party',)
