"""Test for Utils."""

__author__: str = "730476910"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    xs: list[int] = []
    assert only_evens(xs) == []


def test_only_evens_multiple() -> None:
    xs: list[int] = [10, 22, 35, 84]
    assert only_evens(xs) == [10, 22, 84]


def test_only_evens_multiple_odd() -> None:
    xs: list[int] = [33, 55, 77, 99, 111, 13]
    assert only_evens(xs) == []


def test_sub_empty() -> None:
    xs: list = [10, 12, 13]
    first_number: int = 0
    second_number: int = 1
    assert sub(xs, first_number, second_number) == [10]


def test_sub_full_list() -> None:
    xs: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_number: int = 0
    second_number: int = 10
    assert sub(xs, first_number, second_number) == xs


def test_sub_half_list() -> None:
    xs: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    first_number: int = 5
    second_number: int = 10
    assert sub(xs, first_number, second_number) == [6, 7, 8, 9, 10]


def test_concat_empty() -> None:
    xs: list = []
    ys: list = []
    assert concat(xs, ys) == []


def test_concat_small_list() -> None:
    xs: list = [1, 2, 3]
    ys: list = [4, 5, 6]
    assert concat(xs, ys) == [1, 2, 3, 4, 5, 6]


def test_concat_big_list() -> None:
    xs: list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    ys: list = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    results: list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
    assert concat(xs, ys) == results
