"""
Practice with the dictionary built-in data type
and file reading.

File: client.py
Initial developers: COMP 801 instructors
Developer: Swathi Danturi
"""
from scrabble_letters import ScrabbleLetters


def main():
    """
    Demo ScrabbleLetters functionality
    """

    letters_file = "scrabble.csv"

    scrabble = ScrabbleLetters(letters_file)

    word = "help"

    freq = scrabble.get_freq(word)
    points = scrabble.get_points(word)

    print(f"{freq}")
    print(f"{points}")

    scrabble.reduce_freq(word)
    freq = scrabble.get_freq(word)

    print(f"{freq}")


def easy():
    """
    Read the content of the file using readline().
    """
    easy_file = "sample.txt"

    file_object = open(file=easy_file, encoding='UTF-8', mode='r')

    line = file_object.readline()

    while line:
        line = line.strip()
        print(line)
        line = file_object.readline()


def other():
    """
    Read the content of the file iterating throught the file object directly.
    """
    scrabble_file = "scrabble.csv"

    letters_file = open(file=scrabble_file, encoding='UTF-8', mode='r')

    for line in letters_file:
        print(line)


if __name__ == "__main__":
    main()
    other()
    easy()
