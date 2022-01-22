"""EX01 - Chardle"""
__author__ = "73047610"

full_word: str = input("Enter a 5 letter word: ")
if len(full_word) != 5:
    print("Error: word must contain 5 characters")
    exit()
single_letter: str = input("Enter a single letter: ")
if len(single_letter) != 1:
    print("Error: Character must be a single character")
    exit()
count: int = 0

print(f"Searching for {single_letter} in {full_word}.")


if single_letter == full_word[0]:
    print(f"{single_letter} found at index 0")
    count += 1
if single_letter == full_word[1]:
    print(f"{single_letter} found at index 1")
    count += 1
if single_letter == full_word[2]:
    print(f"{single_letter} found at index 2")
    count += 1
if single_letter == full_word[3]:
    print(f"{single_letter} found at index 3")
    count += 1
if single_letter == full_word[4]:
    print(f"{single_letter} found at index 4")
    count += 1

if count > 0:
    print(f"{count} instances of {single_letter} found in {full_word}.")
else:
    print(f"No instances of {single_letter} found in {full_word}")