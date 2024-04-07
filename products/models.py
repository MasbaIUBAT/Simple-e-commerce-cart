from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField(max_length=255)
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2083)


class Offer(models.Model):
    code = models.CharField(max_length=55)
    description = models.CharField(max_length=555)
    discount = models.FloatField
    

