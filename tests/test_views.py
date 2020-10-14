import random
import pytest

from character.api.views import create_rating, retrieve_character
from django.urls import reverse


pytestmark = pytest.mark.django_db


class TestRetrieveCharacter:
    """
    Scenarios related to retrieve_character view
    """
    
    @pytest.mark.parametrize('kwargs, expected_code',[
        ({'id':1},      200),
        ({'id': 12132}, 404),
    ])
    def test_retrieve_character(self, kwargs, expected_code, rf):
        """
        Test all scenarios for retrieve_character view
        """
        
        url = reverse('character:character', kwargs=kwargs)
        request = rf.get(url)

        response = retrieve_character(request, kwargs['id']).render()

        assert response.status_code == expected_code

class TestCreateRating:

    @pytest.mark.parametrize('kwargs, expected_code',[
        ({'id':1},      201),
        ({'id': 12132}, 404),
    ])
    def test_create_rating(self, kwargs, expected_code, rf):
        url = reverse('character:rating', kwargs=kwargs)
        post_data = {
            'character': kwargs['id'],
            'score': random.randrange(1,6)
        }
        request = rf.post(url, post_data)

        response = create_rating(request, kwargs['id']).render()

        assert response.status_code == expected_code