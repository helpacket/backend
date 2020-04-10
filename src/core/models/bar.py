from django.db import models

from .band import Band
from .concert import Concert


class Bar(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    description = models.TextField(blank=True, null=True)
    map_url = models.URLField(max_length=512)

    bands = models.ManyToManyField(Band, related_name='bars', through=Concert)

    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
