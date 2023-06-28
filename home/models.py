from django.db import models

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    info2 = models.CharField(max_length = 100, default = '')
    info3 = models.CharField(max_length = 100, default = '')
    info4 = models.CharField(max_length = 100, default = '')

    def __str__(self):
        return self.name
