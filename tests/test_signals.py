from .conftest import RatingFactory, CharacterStatsFactory
import pytest

class TestRating:
    """
    Rating model signals
    """
    @pytest.mark.django_db
    def test_calculate_new_rating_stats(self):
        character = CharacterStatsFactory()
        RatingFactory.create_batch(2, character=character, score=3)

        assert character.average_rating == 3.00
        assert character.max_rating == 3.00