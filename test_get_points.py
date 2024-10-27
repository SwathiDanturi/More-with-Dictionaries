"""
Test get_points methods of scrabble_letters

File: test_get_points.py
Developer: Swathi Danturi
"""

import pytest
from scrabble_letters import ScrabbleLetters


def test_get_points_for_word_without_blank():
    """
    Testing get_points of scrabble_letters.py without the space in a word
    """
    file_path = "C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv"
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual = test_scrabble_letters.get_points("homework")
    expected = 20
    assert actual == expected


def test_get_points_for_word_with_blank():
    """
    Testing get_points of scrabble_letters.py with space in a word
    """
    file_path = "C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv"
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual = test_scrabble_letters.get_points("homework start")
    expected = 25
    assert actual == expected


pytest.main()
