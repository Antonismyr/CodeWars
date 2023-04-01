import string
def alphabet_position(text):
    letters = list(string.ascii_lowercase)
    return " ".join([str(letters.index(i)+1) for i in list(text.lower()) if i in letters])