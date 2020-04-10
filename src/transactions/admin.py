from django.contrib import admin
from .models import Request
from .models import Supply
from .models import Transaction


@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_datetime', 'product')


@admin.register(Supply)
class SupplyAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_datetime', 'product')

    class Meta:
        verbose_name_plural = "Supplies"


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('id', 'creation_datetime', )
