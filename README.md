# hangman-test

A small terminal hangman game, used as a fixture for testing an automated
bug-triage pipeline.

## Play

```
python3 hangman.py
```

Guess one letter at a time. Six misses and you lose. Type `q` to give up.

## Test

```
python3 -m pytest tests/ -q
```
