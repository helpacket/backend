from django.db import models


class Transaction(models.Model):
    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)

    request = models.OneToOneField('transactions.Request', on_delete=models.CASCADE)
