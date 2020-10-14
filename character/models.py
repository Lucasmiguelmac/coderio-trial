from django.db import models
from decimal import Decimal


class CharacterStats(models.Model):
    character       = models.IntegerField(primary_key=True, null=False)
    rating_sum      = models.IntegerField(default=0, null=False)
    times_rated     = models.IntegerField(default=0, null=False)
    average_rating  = models.DecimalField(null=True, decimal_places=2, max_digits=3)
    max_rating      = models.IntegerField(null=True)


class Rating(models.Model):
    """
    Rating of a SW character that goes from 1 to 5
    """
    character   = models.ForeignKey(CharacterStats, on_delete=models.PROTECT)
    score       = models.IntegerField()

    def __str__(self):
        return f'{self.character.character}: {self.score}/5'