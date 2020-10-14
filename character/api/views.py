from requests.models import InvalidURL
from rest_framework import serializers
from character.api.serializers import CharacterSerializer, HomeworldSerializer, RatingSerializer
import requests
from ..models import CharacterStats, Rating
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def retrieve_character(request, id):
    try:

        url = f'https://swapi.dev/api/people/{str(id)}/'
        response = requests.get(url)

        if response.status_code == 404:
            data = {
                'message': 'Could not find specified character'
            }
            return Response(data=data, status=response.status_code)

        character_stats = CharacterStats.objects.get_or_create(character=id)[0]
        character_data = response.json()

        homeworld_url = character_data['homeworld']
        homeworld_response = requests.get(homeworld_url)
        homeworld_data = homeworld_response.json()
        homeworld_data['known_residents_count'] = len(homeworld_data['residents'])
        homeworld_serializer = HomeworldSerializer(data=homeworld_data)
        
        if homeworld_serializer.is_valid():
            character_data['homeworld'] = homeworld_serializer.validated_data
        else:

            raise Exception

        try:
            species_url = character_data['species']
            species_response = requests.get(species_url)
            species_data = species_response.json()
            character_data['species_name'] = species_data['name']
        except InvalidURL:
            character_data['species_name'] = 'human'

        character_data['average_rating']  = character_stats.average_rating
        character_data['max_rating']      = character_stats.max_rating

        serializer = CharacterSerializer(data=character_data)
        if serializer.is_valid():
            serialized_data = serializer.validated_data
            return Response(data=serialized_data, status=response.status_code)
        else:

            raise Exception

    except Exception as e:
        data = {
            'message': 'There was an internal error, please contact a Star Wars representative.',
        }
        return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['POST'])
def create_rating(request, id):
    try:

        url = f'https://swapi.dev/api/people/{str(id)}/'
        response = requests.get(url)

        if response.status_code == 404:
            data = {
                'message': 'Could not find specified character'
            }
            return Response(data=data, status=response.status_code)

        character = CharacterStats.objects.get_or_create(character=id)[0]
        score = request.data['score']
        rating = Rating(character=character, score=score)
        rating.save()
        data = {
            'message': 'Character succesfully rated!'
        }
        return Response(data=data, status=status.HTTP_201_CREATED)
    
    except Exception as e:
        data = {
            'message': 'There was an internal error, please contact a Star Wars representative.',
        }
        return Response(data=data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)