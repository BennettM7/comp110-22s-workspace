"""Tests for Dictionary functions."""

__author__: str = "730476910"

from dictionary import invert
from dictionary import count


def test_invert_empty() -> None:
    """Tests to see if invert will return an empty dictionary."""
    xs: dict[str, str] = {}
    assert invert(xs) == {}


def test_invert_small() -> None:
    """Tests to see if invert will return a small dictionary inverted."""
    xs: dict[str, str] = {'apple': 'cat'}
    assert invert(xs) == {'cat': 'apple'}


def test_invert_big() -> None:
    """Tests to see if it can take more than one entry."""
    xs: dict[str, str] = {'1': '10', '2': '9', '3': '8', '4': '7', '5': '6'}
    assert invert(xs) == {'10': '1', '9': '2', '8': '3', '7': '4', '6': '5'}


def test_count_empty() -> None:
    """Tests to see if count can take a empty list."""
    xs: list[str] = []
    assert count(xs) == {}


def test_count_small() -> None:
    """Tests to see if count can handle one repeated word and one single word."""
    xs: list[str] = ['Hello', 'Bennett', 'Hello']
    assert count(xs) == {
        'Hello': 2, 
        'Bennett': 1
    }


def test_count_big() -> None:
    """Tests to see if it can take a large list and confine it down to it's repeated words."""
    xs: list[str] = ['Hello', 'Hello', 'Bennett', 'Bennett', 'World', 'World', 'World', 'World']
    assert count(xs) == {
        'Hello': 2,
        'Bennett': 2,
        'World': 4
    }