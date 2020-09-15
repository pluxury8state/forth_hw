from django.db import models


class Phone(models.Model):
    name = models.SlugField()
    price = models.FloatField()
    image = models.TextField()
    release_date = models.TextField()
    lte_exists = models.BooleanField()

