import factory
import random
from factory import faker
import pytest

from decimal import Decimal
from itertools import chain
from character.models import CharacterStats, Rating
from factory.django import DjangoModelFactory


#======================================FACTORIES=======================================
class CharacterStatsFactory(DjangoModelFactory):
    class Meta:
        model = CharacterStats
    character       = factory.Faker('random_number')

class RatingFactory(DjangoModelFactory):
    class Meta:
        model = Rating
    character   = factory.SubFactory(CharacterStatsFactory)
    score       = random.randrange(1, 6)

#=======================================FIXTURES=======================================
@pytest.fixture
def charstats():
    return CharacterStatsFactory(character=1)

@pytest.fixture
def hw_dict():
    hw = {
        'name': 'Testooine',
        'population': random.randrange(1, 1000000000, 100000),
        'known_residents_count': random.randrange(1, 40, 2),
    }
    return hw

@pytest.fixture
def char_dict():
    char = {
        'name': 'Darth Tester',
        'height': random.randrange(50, 400, 10),
        'mass': random.randrange(50, 400, 2),
        'hair_color': factory.Faker('color'),
        'skin_color': factory.Faker('color'),
        'eye_color': factory.Faker('color'),
        'birth_year': str(random.randint(1, 1000)) + random.choice(['BBY', 'ABY']),
        'gender': random.choice(['male', 'female', 'other']),
        'homeworld': hw_dict(),
        'species_name': factory.Faker('sentence', nb_words=1),
        'average_rating': float(Decimal(random.randrange(1, 6))),
        'max_rating': random.randrange(1, 6)
    }