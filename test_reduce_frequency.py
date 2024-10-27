"""
Test reduce_frequency methods of scrabble_letters

File: test_reduce_frequency.py
Developer: Swathi Danturi
"""

import pytest
from scrabble_letters import ScrabbleLetters


def test_reduce_frequency_for_j():
    """
    Testing reduce_frequency of scrabble_letters.py for the character 'j'
    """
    file_path = "C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv"
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual1 = test_scrabble_letters.reduce_freqeuncy("j")
    actual2 = test_scrabble_letters.reduce_freqeuncy("j")
    expected = (True, False)
    actual = (actual1, actual2)
    assert actual == expected


def test_reduce_frequency_for_blank():
    """
    Testing reduce_frequency of scrabble_letters.py for blank space
    """
    file_path = "C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv"
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual1 = test_scrabble_letters.reduce_freqeuncy(" ")
    actual2 = test_scrabble_letters.reduce_freqeuncy(" ")
    actual3 = test_scrabble_letters.reduce_freqeuncy(" ")
    expected = (True, True, False)
    actual = (actual1, actual2, actual3)
    assert actual == expected


pytest.main()
