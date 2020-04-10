from django.db import models


class Concert(models.Model):
    id = models.AutoField(primary_key=True)
    start_datetime = models.DateTimeField()
    cost = models.PositiveIntegerField(default=0)

    bar = models.ForeignKey('core.Bar', related_name='concerts', null=True, on_delete=models.SET_NULL)
    band = models.ForeignKey('core.Band', related_name='concerts', null=True, on_delete=models.SET_NULL)
    creator = models.ForeignKey('users.Person', related_name="concerts", null=True, on_delete=models.SET_NULL)

    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)
