import pytest
# from character.api.serializers import HomeworldSerializer, CharacterSerializer, RatingSerializer
from .conftest import RatingFactory, charstats


from character.api.serializers import HomeworldSerializer, RatingSerializer
from rest_framework import serializers
from tests.conftest import hw_dict


class TestHomeworld:
    
    def test_homeworld_serialization(self, hw_dict):
        """
        Serialization of a request body works as expected
        """

        working_serializer = HomeworldSerializer(data=hw_dict)
        working_serializer.is_valid()
        assert not working_serializer.errors

        broken_data = hw_dict.pop('name')
        broken_serializer = HomeworldSerializer(data=broken_data)
        assert not broken_serializer.is_valid()

    
class TestRating:

    @pytest.mark.django_db
    def test_single_object_serialization(self, charstats):
        """
        Can properly serialize a Rating object
        """
        rating = RatingFactory(character=charstats, score=3)
        serializer = RatingSerializer(rating)

        assert set(dict(serializer.data).keys()) == {'character', 'score'}