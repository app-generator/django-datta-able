from django.db import models

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100)
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    recipient_address = models.JSONField()
    package_details = models.JSONField()
    tracking_number = models.CharField(max_length=50)