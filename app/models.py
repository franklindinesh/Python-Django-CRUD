from django.db import models


# Create your models here.
class ProductTable(models.Model):
    name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    price = models.IntegerField()