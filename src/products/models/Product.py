from django.db import models


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)

    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name
