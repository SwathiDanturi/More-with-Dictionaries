"""
Practice with the dictionary built-in data type.

File: scrabble_letters.py
Initial developers: COMP 801 instructors
Developer: Swathi Danturi
"""


class ScrabbleLetters:
    """
    Stores letters used in a game of Scrabble.  The letters are stored in a
    dictionary that includes frequency and point values.
    Frequency values give the number of times a Scrabble tile showing that
    letter is included in the game. Point values give the points for the given
    letter.  The dictionary format is as follows:

        { letter: [frequency, points], ... }

    The class contains methods to look up the pointvalue of a word, reduce
    the frequency of a letter (because it has been used in the game) and to
    retrieve the frequency of letters in order to keep track of how many
    letters remain.

    The class treats lowercase and uppercase letters the same.  For example,
    'A' is the same as 'a' from the point of view of the client code.

    The file includes a blank letter.  Strings passed to the class will use an
    underscore to indicate a blank letter. In the following example, a blank
    is put in the place of the lower case l for the string Hello:

        word = "Hel_o"
    """

    def __init__(self, scrabble_file):
        """
        Attribute: self.letters, dictionary
            Keys: Strings, representing letters. The programmer chooses the
            internal representation of the "blank" letter.
            Values: The freqeuncy and point value of the letter

            For example, the first lines of a Scrabble file are:

                a,9,1
                b,2,3
                c,2,3

            This will produce the start of the letters dictionary:

                { 'a': [9, 1], 'b': [2, 3], 'c': [2, 3], ... }

        :param: a string representing the path to the Scrabble file.

            The file stores letters, the freqency of the letter and the score
            for the letter in comma delimited strings.
            For example, the first letter in the file is 'a',
            nine tiles contain an 'a' and the 'a' is worth one point:

                a,9,1
        """
        self.scrabble_letters = {}

        with open(scrabble_file, encoding="UTF-8", mode="r") as letters_file:
            for line in letters_file:
                print(line)
                line = line.strip()
                letter, count, points = line.split(",")
                if letter == "blank":
                    letter = " "
                if count.isdigit() and points.isdigit():
                    count = int(count)
                    points = int(points)
                    self.scrabble_letters[letter] = [count] + [points]
        letters_file.close()

    def reduce_freqeuncy(self, letter: str) -> bool:
        """
        Reduces the frequency of the given letter if the letter frequency is
        greater than zero.

        :param letter: One letter in the form of a string. The letter may be
        'A' to 'Z', 'a' to 'z' or '_' (blank).
        :return: True if the letter frequency was reduced, False otherwise.
        """
        letter = letter.lower()
        if self.scrabble_letters[letter][0] > 0:
            self.scrabble_letters[letter][0] -= 1
            return True
        return False

    def get_freq(self, letters: str) -> dict:
        """
        :param letters: a sequence of letters in the form of a string.
        :return: A dictionary containing the frequency of
        each letter.  For example, if no frequencies have been reduced:
            The input "abc" will return {'a': 9, 'b' : 2, 'c': 2 }
        """
        letters_frequency = {}
        for char in letters:
            letters_frequency[char] = self.scrabble_letters[char][0]
        return letters_frequency

    def get_points(self, word: str) -> int:
        """
        :param word: a sequence of letters in the form of a string.
        :return: An integer containing the total points for the word.
        """
        total_points = 0
        for char in word:
            total_points += self.scrabble_letters[char][1]
        return total_points
