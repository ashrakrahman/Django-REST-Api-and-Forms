from __future__ import unicode_literals
from django.db import models

class Product (models.Model):
    product_name = models.CharField(max_length=255,default="")
    product_description = models.CharField(max_length=1000,default="")
    product_price = models.IntegerField(default=0)
    company_name =  models.CharField(max_length=255, default="")
    company_country = models.CharField(max_length=255,default="")
    product_bid = models.IntegerField(default=0)


    def __str__(self):
        return self.product_name

