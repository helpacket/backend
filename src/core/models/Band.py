from django.db import models


class Band(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    image_url = models.URLField(max_length=512, null=True, blank=True)

    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)

    owner = models.ForeignKey('parties.Person', related_name="bands", null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.name
