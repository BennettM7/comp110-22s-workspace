"""Test for Utils."""

__author__: str = "730476910"

from utils import only_evens
from utils import sub
from utils import concat


def test_only_evens_empty() -> None:
    """Tests an empty list."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_multiple() -> None:
    """Tests a list with a lot of even numbers."""
    xs: list[int] = [10, 22, 35, 84]
    assert only_evens(xs) == [10, 22, 84]


def test_only_evens_multiple_odd() -> None:
    """Tests a list with all odds and no even numbers."""
    xs: list[int] = [33, 55, 77, 99, 111, 13]
    assert only_evens(xs) == []


def test_sub_empty() -> None:
    """Test for the first integer."""
    xs: list[int] = [10, 12, 13]
    first_number: int = 0
    second_number: int = 1
    assert sub(xs, first_number, second_number) == [10]


def test_sub_full_list() -> None:
    """Tests for the full list returned."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_number: int = 0
    second_number: int = 10
    assert sub(xs, first_number, second_number) == xs


def test_sub_half_list() -> None:
    """Tests to see if it returns half of the list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_number: int = 5
    second_number: int = 10
    assert sub(xs, first_number, second_number) == [6, 7, 8, 9, 10]


def test_sub_negative_start() -> None:
    """Tests to see if it can take a negative starting integer."""
    xs: list[int] = [1, 2, 3, 4, 5]
    first_number: int = -1
    second_number: int = 5
    assert sub(xs, first_number, second_number) == [1, 2, 3, 4, 5]


def test_sub_last_number_greater() -> None:
    """Tests to see if it can take a number larger than the length of the list."""
    xs: list[int] = [1, 2, 3, 4, 5]
    first_number: int = 0
    second_number: int = 6
    assert sub(xs, first_number, second_number) == [1, 2, 3, 4, 5]


def test_concat_empty() -> None:
    """Tests to see if the function returns an empty list."""
    xs: list[int] = []
    ys: list[int] = []
    assert concat(xs, ys) == []


def test_concat_small_list() -> None:
    """Tests to see if the function returns a small list."""
    xs: list[int] = [1, 2, 3]
    ys: list[int] = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_big_list() -> None:
    """Tests to see if it returns a large list."""
    xs: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ys: list[int] = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    results: list[int] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert concat(xs, ys) == results
