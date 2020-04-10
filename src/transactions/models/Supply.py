from django.db import models


class Supply(models.Model):
    PENDING = 0
    ASSIGNED = 1
    SENT = 2
    STATUS_CHOICES = (
        (PENDING, 'pending'),
        (ASSIGNED, 'assigned'),
        (SENT, 'sent'),
    )

    id = models.AutoField(primary_key=True)
    creation_datetime = models.DateTimeField(auto_now_add=True)
    last_modification_datetime = models.DateTimeField(auto_now=True)

    product = models.ForeignKey('products.Product', related_name='supplies', on_delete=models.CASCADE)
    # supplier = models.ForeignKey(Supplier, related_name='supplies', on_delete=models.CASCADE)
    transaction = models.ForeignKey('transactions.Transaction', related_name='supplies', null=True, blank=True, on_delete=models.SET_NULL)

    amount = models.IntegerField()
    status = models.IntegerField(
        choices=STATUS_CHOICES,
        default=PENDING,
    )
