"""EX03 - Wordle Project."""
__author__: str = "730476910"


def contains_char(word_search: str, char_search: str) -> bool:
    """Returns True if the single character of the second string is found at any index."""
    assert len(char_search) == 1
    if char_search in word_search:
        return True
    else:
        return False


def emojified(word_guess: str, sec_word: str) -> str:
    """Returns the emoji's used in wordle to tell you what is right and wrong."""
    assert len(word_guess) == len(sec_word)
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    i = 0
    boxes: str = ""
    
    while i < len(word_guess):
        if word_guess[i] == sec_word[i]:
            boxes += f"{GREEN_BOX}"
            i += 1
        else:
            if contains_char(sec_word, word_guess[i]):
                boxes += f"{YELLOW_BOX}"
            else:
                boxes += f"{WHITE_BOX}"
            i += 1
    return boxes


def input_guess(guess_length: int) -> str:
    """Checks the length of the word."""
    user_input: str = input(f"Enter a {guess_length} charcter word: ")
    while len(user_input) != guess_length:
        user_input = input(f"that wasn't {guess_length} chars! Try again: ")
    return user_input


def main() -> None:
    """The entry point of the program and mian game loop."""
    max_turns: int = 6
    turns_taken: int = 1
    secret_word: str = "codes"
    correct_answer: str = "\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9\U0001F7E9"
    while turns_taken <= max_turns:
        print(f"=== turns {str(turns_taken)}/{str(max_turns)} ===")
        # input_guess(5)
        user_guess: str = input_guess(5)
        emojis: str = emojified(user_guess, secret_word)
        if emojis == correct_answer:
            print(emojis)
            print(f"You won in {turns_taken}/{max_turns} turns!")
            break
        else:
            print(emojis)
            turns_taken += 1
    if turns_taken == 7:
        print(f"X/{max_turns} - Sorry, try again tomorrow!")


__name__: str = "__main__"
if __name__ == "__main__":
    main()