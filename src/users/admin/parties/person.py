"""Set of admin instantiations."""

from django.contrib.admin import register
from django.contrib.auth.admin import UserAdmin

from ...models import Person


@register(Person)
class PersonAdmin(UserAdmin):
    pass
