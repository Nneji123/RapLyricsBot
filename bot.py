import time
import random

# simple function to read a text file and print out random lines


def print_random_lines(filename: str):
    """
    The print_random_lines function prints a random line from the file specified by filename.
       The function takes one argument, filename.

    Args:
        filename:str: Pass the name of the file to be opened

    Returns:
        The number of lines in the file

    Doc Author:
        Ifeanyi
    """
    count = 0
    f = open(filename, encoding='utf8')
    lines = f.readlines()
    for line in lines:
        count += 1
        rand_line = random.randint(0, len(lines)-1)  # this should make it work
        print(lines[rand_line])
        time.sleep(5)


files = 'drake_lyrics.txt'
print_random_lines(files)
