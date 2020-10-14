from decimal import Decimal
from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Rating


@receiver(post_save, sender=Rating)
def calculate_new_rating_stats(sender, instance, *args, **kwargs):
    """
    Calculate new max rating and new average rating.
    """
    character = instance.character
    character.times_rated += 1
    character.rating_sum += int(instance.score)
    character.average_rating = float(Decimal(character.rating_sum / character.times_rated))
    if character.max_rating == None:
        character.max_rating = instance.score
    elif character.max_rating < instance.score:
        character.max_rating = instance.score

