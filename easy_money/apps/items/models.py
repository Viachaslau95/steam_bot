from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    price_4 = models.FloatField()
    is_active = models.BooleanField()
    is_testing = models.BooleanField()
    link = models.TextField()
    image = models.ImageField()
