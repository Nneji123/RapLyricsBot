import random
# function for reading lines of a string


def create_lyric(filename: str):
    """
    This function prints a random line from the file specified by filename which is drake lyrics in this case. It also exludes lines that have specific words in a list

    The function takes one argument, filename.

    Args:
        filename:str: Pass the name of the file to be opened

    Returns:
        The contents of each line in the file.

    Doc Author:
        Ifeanyi
    """
    count = 0
    while True:
        with open(filename, encoding="utf8") as f:
            lines = f.readlines()
        for line in lines:
            count += 1
            rand_line = random.randint(0, len(lines) - 1)
            line = lines[rand_line]
            strings = ['Verse', 'Chorus', 'Interlude', 'Produced',
                       'Bridged', 'Intro', 'Outro']
            words = line.split()
            resultwords = [word for word in words if word.lower()
                           not in strings]
            if resultwords != "" and len(resultwords) > 10:
                return ('Tweeting a lyric...')
            else:
                pass
