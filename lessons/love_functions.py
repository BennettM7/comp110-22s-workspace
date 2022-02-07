"""Love function in class"""


def love(name: str) -> str:
    """Given a name as a parameter, returns a love string."""
    return f"I love you {name}"


def spread_love(to: str, n: int) -> str:
    """Generates a string that repeats a loing message n times."""
    counter: int = 0
    love_note: str = ""
    while counter < n:
        love_note += love(to) + "\n"
        counter += 1
    return love_note
