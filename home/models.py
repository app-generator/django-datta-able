from django.db import models

# Create your models here.

class Product(models.Model):
    id    = models.AutoField(primary_key=True)
    name  = models.CharField(max_length = 100) 
    info  = models.CharField(max_length = 100, default = '')
    price = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Site(models.Model):
    site_id = models.CharField(unique=True, max_length=5, blank=True, null=True)
    site_name = models.CharField(max_length=250, blank=True, null=True)
    url = models.CharField(max_length=250, blank=True, null=True)
    sitecol = models.CharField(max_length=45, blank=True, null=True)
    lat = models.CharField(max_length=45, blank=True, null=True)
    long = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'site'
        ordering = ('site_name',)

    def __str__(self):
        return self.site_name
   