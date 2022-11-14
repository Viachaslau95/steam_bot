from django.db import models


class Item(models.Model):
    title = models.CharField(max_length=255)
    price_4 = models.FloatField(blank=True, null=True)
    price_for_name_tag = models.FloatField(blank=True, null=True)
    is_active = models.BooleanField()
    is_testing = models.BooleanField()
    link = models.TextField()
    image = models.ImageField()
