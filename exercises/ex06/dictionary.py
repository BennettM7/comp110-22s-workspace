"""EX06 - Geting some practice with Dictionaries."""


__author__: str = "730476910"


def invert(given_dict: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in a dictionary."""
    inv_dict: dict[str, str] = {}
    for key in given_dict:
        inv_dict[given_dict[key]] = key
    return inv_dict


def favorite_color(given_dict: dict[str, str]) -> str:
    """Need help with this."""
    new_dict: dict[str, int] = {}
    for key in given_dict:
        if given_dict[key] in new_dict:
            new_dict[given_dict[key]] += 1
        else:
            new_dict[given_dict[key]] = 1
    return ''
        

def count(given_list: list[str]) -> dict[str, int]:
    """Counts how many repeated items in a list there are."""
    list_to_dict: dict[str, int] = {}
    for item in given_list:
        if item in list_to_dict:
            list_to_dict[item] += 1
        else:
            list_to_dict[item] = 1
    return list_to_dict
