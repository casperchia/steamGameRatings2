from django.db import models
from math import sqrt


class Game(models.Model):
    appid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    positive = models.IntegerField(default=0)
    negative = models.IntegerField(default=0)
    rating = models.DecimalField(max_digits=5, decimal_places=2, editable=False)
    wilson = models.DecimalField(max_digits=5, decimal_places=2, editable=False)

    def save(self):
        self.rating = float(self.positive) * 100 / (self.positive + self.negative)
        self.wilson = (((float(self.positive) + 1.9208) / (float(self.positive) + float(self.negative)) - 1.96 * sqrt((float(self.positive) * float(self.negative)) / (float(self.positive) + float(self.negative)) + 0.9604) / (float(self.positive) + float(self.negative))) / (1 + 3.8416 / (float(self.positive) + float(self.negative)))) * 100
        super(Game, self).save()
