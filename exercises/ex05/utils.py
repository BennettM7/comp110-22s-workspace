"""EX05 - building some list utility functions."""

__author__: str = "730476910"


def only_evens(old_list: list[int]) -> list:
    new_list: list = []
    for x in old_list:
        if x % 2 == 0:
            new_list.append(x)
    return new_list


def sub(old_list: list, first_int: int, second_int: int) -> list:
    new_list: list = []
    for x in old_list:
        while first_int != second_int:
            new_list.append(old_list[first_int])
            first_int += 1
    return new_list


def concat(first_list: list[int], second_list: list[int]) -> list[int]:
    new_list: list[int] = []
    for x in first_list:
        new_list.append(x)
    for x in second_list:
        new_list.append(x)
    return new_list