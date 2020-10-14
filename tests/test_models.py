from .conftest import CharacterStatsFactory, RatingFactory, charstats
from character.models import CharacterStats, Rating
from faker import Faker
# from .conftest import HomeworldFactory, SpeciesFactory, CharacterFactory, RatingFactory

import pytest


pytestmark = pytest.mark.django_db # We set the mark for all tests


class TestCharacterStats:
    """
    Tests for the CharacterStats model
    """
    
    def test_create_charstats(self, charstats):
        """
        CharacterStats can be created
        """
        character = charstats.character
        assert CharacterStats.objects.all().count() == 1
        assert CharacterStats.objects.all().last().character


class TestRating:

    def test_rating__str__(self, charstats):
        """
        Rating str() representation is the expected
        """
        rating = RatingFactory(character=charstats)

        assert Rating.objects.all().count() == 1
        assert str(rating) == f'1: {rating.score}/5'


