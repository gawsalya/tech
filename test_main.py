import pytest
import random

from main import points_from_letters, assign_seven_random_tiles, return_valid_word


def test_if_points_is_10():
    result = points_from_letters('GUARDIAN')

    assert result == 10


def test_if_input_is_string():
    with pytest.raises(TypeError):
        result = points_from_letters(1245)


def test_assigns_seven_tiles():
    result = assign_seven_random_tiles()

    assert len(result) == 7


def test_returns_word_():
    random.seed(236577)
    tiles = assign_seven_random_tiles()
    result = return_valid_word(tiles)

    assert result == 'SURE'
