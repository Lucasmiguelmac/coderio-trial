from django.db.models import fields
from character.models import Rating
from rest_framework import serializers

class HomeworldSerializer(serializers.Serializer):
    name                    = serializers.CharField()
    population              = serializers.IntegerField()
    known_residents_count   = serializers.IntegerField()

class CharacterSerializer(serializers.Serializer):
    name            = serializers.CharField(max_length=150)
    height          = serializers.IntegerField(allow_null=True)
    mass            = serializers.IntegerField(allow_null=True)
    hair_color      = serializers.CharField(allow_null=True, max_length=30)
    skin_color      = serializers.CharField(allow_null=True, max_length=30)
    eye_color       = serializers.CharField(allow_null=True, max_length=30)
    birth_year      = serializers.CharField(allow_null=True, max_length=11) # Universe was created on 27M BBY
    gender          = serializers.CharField(allow_null=True)
    homeworld       = HomeworldSerializer(allow_null=True)
    species_name    = serializers.CharField(allow_null=True)
    average_rating  = serializers.DecimalField(allow_null=True, max_digits=3, decimal_places=2)
    max_rating      = serializers.IntegerField(allow_null=True)

class RatingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        exclude = ('id',)