from os import name
from django.urls import path, include
from .views import retrieve_character, create_rating

app_name = 'character'

urlpatterns = [
    path('character/<int:id>/',         retrieve_character, name='character'),
    path('character/<int:id>/rating',   create_rating,      name='rating'),
]