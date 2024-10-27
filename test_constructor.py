"""
Test constructor of scrabble_letters

File: test_constructor.py
Developer: Swathi Danturi
"""

import pytest
from scrabble_letters import ScrabbleLetters


def test_init_constructor_with_path():
    """
    Testing constructor of scrabble_letters.py with absolute path of the file
    """
    file_path = "C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv"
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual = test_scrabble_letters.scrabble_letters
    expected = {
        "a": [9, 1],
        "b": [2, 3],
        "c": [2, 3],
        "d": [4, 2],
        "e": [12, 1],
        "f": [2, 4],
        "g": [3, 2],
        "h": [2, 4],
        "i": [9, 1],
        "j": [1, 8],
        "k": [1, 5],
        "l": [4, 1],
        "m": [2, 3],
        "n": [6, 1],
        "o": [8, 1],
        "p": [2, 3],
        "q": [1, 10],
        "r": [6, 1],
        "s": [4, 1],
        "t": [6, 1],
        "u": [4, 1],
        "v": [2, 4],
        "w": [2, 4],
        "x": [1, 8],
        "y": [2, 4],
        "z": [1, 10],
        " ": [2, 0],
    }
    assert actual == expected


def test_init_constructor_with_filename():
    """
    Testing constructor of scrabble_letters.py with the file name
    """
    test_scrabble_letters = ScrabbleLetters("scrabble.csv")
    actual = test_scrabble_letters.scrabble_letters
    expected = {
        "a": [9, 1],
        "b": [2, 3],
        "c": [2, 3],
        "d": [4, 2],
        "e": [12, 1],
        "f": [2, 4],
        "g": [3, 2],
        "h": [2, 4],
        "i": [9, 1],
        "j": [1, 8],
        "k": [1, 5],
        "l": [4, 1],
        "m": [2, 3],
        "n": [6, 1],
        "o": [8, 1],
        "p": [2, 3],
        "q": [1, 10],
        "r": [6, 1],
        "s": [4, 1],
        "t": [6, 1],
        "u": [4, 1],
        "v": [2, 4],
        "w": [2, 4],
        "x": [1, 8],
        "y": [2, 4],
        "z": [1, 10],
        " ": [2, 0],
    }
    assert actual == expected


def test_init_constructor_with_differentfile():
    """
    Testing constructor of scrabble_letters.py
    with the dummy file scrabble_test.csv
    """
    test_scrabble_letters = ScrabbleLetters("scrabble_test.csv")
    actual = test_scrabble_letters.scrabble_letters
    expected = {"a": [9, 1], "b": [2, 3], "c": [2, 3], "d": [4, 2], "e": [12, 1]}
    assert actual == expected


pytest.main()
