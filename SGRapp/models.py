from django.db import models


class Game(models.Model):
    appid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2)
