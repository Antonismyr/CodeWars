import string
def find_missing_letter(chars):
    letters = list(string.ascii_lowercase)
    letters = [i.upper() for i in letters] if chars[0].isupper() else letters
    return [i for i in letters[letters.index(chars[0]):letters.index(chars[-1])] if i not in chars][-1]