"""EX02 - one shot worldle."""
__author__: str = "730476910"

secret_word: str = "python"
user_guess: str = input(f"Enter a {len(secret_word)}-letter word: ")
WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"
i: int = 0
results_of_guess: str = ""


while len(user_guess) != len(secret_word):
    user_guess = input(f"That was not {len(secret_word)} letters! try again: ")

while i < len(secret_word):
    if user_guess[i] == secret_word[i]:
        results_of_guess += f"{GREEN_BOX}"
    elif user_guess[i] != secret_word[i] and user_guess[i] in secret_word:
        results_of_guess += f"{YELLOW_BOX}"
    else:
        results_of_guess += f"{WHITE_BOX}"
    i += 1

print(results_of_guess)
if user_guess == secret_word:
    print("Woo! You got it!")
else:
    print("Not quite. Play again soon!")