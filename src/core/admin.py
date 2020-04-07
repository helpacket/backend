from django.contrib import admin
from core.models import Bar, Concert, Band


@admin.register(Bar)
class BarAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ('bar', 'band', 'start_datetime',)


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ('name', )
