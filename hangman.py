#!/usr/bin/env python3
"""A small terminal hangman game.

Pick a word, guess letters, don't run out of lives.
"""

import random
import sys

from words import WORDS

MAX_MISSES = 6

GALLOWS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ===""",
]

# Typing "q" at the prompt leaves the game early.
QUIT_KEY = "q"


def masked(word, guessed):
    """The word with unguessed letters hidden."""
    return " ".join(letter if letter in guessed else "_" for letter in word)


def is_won(word, guessed):
    return all(letter in guessed for letter in word)


def prompt_guess(guessed):
    """Read one letter from the player, re-prompting until it is usable."""
    while True:
        raw = input("Guess a letter: ").strip().lower()

        if raw == QUIT_KEY:
            return None

        if len(raw) != 1 or not raw.isalpha():
            print("  Please enter a single letter.")
            continue

        if raw in guessed:
            print(f"  You already guessed '{raw}'.")
            continue

        return raw


def play(word):
    guessed = set()
    misses = 0

    print("\nH A N G M A N")
    print(f"The word has {len(word)} letters. Type '{QUIT_KEY}' to give up.\n")

    while misses < MAX_MISSES:
        print(GALLOWS[misses])
        print(f"\n  {masked(word, guessed)}")
        if guessed:
            print(f"  guessed: {' '.join(sorted(guessed))}")
        print(f"  lives:   {MAX_MISSES - misses}\n")

        guess = prompt_guess(guessed)

        if guess is None:
            print(f"\nGiving up. The word was '{word}'.")
            sys.exit(0)

        guessed.add(guess)

        if guess in word:
            print(f"  Yes, there's a '{guess}'.\n")
            if is_won(word, guessed):
                print(f"You got it: {word}")
                return True
        else:
            misses += 1
            print(f"  No '{guess}' in it.\n")

    print(GALLOWS[MAX_MISSES])
    print(f"\nOut of lives. The word was '{word}'.")
    return False


def main():
    word = random.choice(WORDS)
    play(word)


if __name__ == "__main__":
    main()
