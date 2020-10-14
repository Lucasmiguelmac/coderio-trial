import pytest

from django.urls import reverse, resolve


class TestURLs:
    """
    Test urls
    """
    @pytest.mark.parametrize('url_name, expected_path, kwargs, viewname',[
        ('character:character', '/api/character/1/',         {'id':1},   'retrieve_character'),
        ('character:rating',    '/api/character/1/rating',  {'id':1},   'create_rating'),
        
    ])
    def test_character_app(self, url_name, expected_path, kwargs, viewname):
        """
        Assert character app's urls:
        - Have the expected url path
        - Are matched to the proper view function
        """
        url = reverse(url_name, kwargs=kwargs)
        assert url == expected_path

        resolver = resolve(expected_path)
        assert resolver.func.__name__ == viewname