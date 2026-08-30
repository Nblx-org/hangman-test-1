"""Tests for the word-state helpers.

These cover the display and win logic. Input handling is not covered — it reads
from stdin, and nobody got round to wiring up a fake for it.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from hangman import is_won, masked


def test_masked_hides_unguessed():
    assert masked("banjo", set()) == "_ _ _ _ _"


def test_masked_reveals_guessed():
    assert masked("banjo", {"b", "o"}) == "b _ _ _ o"


def test_masked_handles_repeats():
    assert masked("kettle", {"e", "t"}) == "_ e t t _ e"


def test_is_won_when_all_letters_guessed():
    assert is_won("banjo", {"b", "a", "n", "j", "o"})


def test_is_not_won_with_a_letter_missing():
    assert not is_won("banjo", {"b", "a", "n", "j"})
