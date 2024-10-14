"""
Test get_freq methods of scrabble_letters

File: test_get_freq.py
Developer: Swathi Danturi
"""

import pytest
from scrabble_letters import ScrabbleLetters


def test_get_freq_for_word_without_blank():
    """
    Testing get_freq of scrabble_letters.py without the space in a word
    """
    file_path = 'C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv'
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual = test_scrabble_letters.get_freq('user')
    expected = {'u': 4, 's': 4, 'e': 12, 'r': 6}
    assert actual == expected


def test_get_freq_for_word_with_blank():
    """
    Testing get_freq of scrabble_letters.py with space in a word
    """
    file_path = 'C:/Users/Swath/courses/comp801/homework/h2/scrabble.csv'
    test_scrabble_letters = ScrabbleLetters(file_path)
    actual = test_scrabble_letters.get_freq('h i')
    expected = {'h': 2, ' ': 9, 'i': 2}
    assert actual == expected


pytest.main()
