import string 
def pig_it(text):
    marks = string.punctuation
    return " ".join([i[1:] + i[0] + 'ay' if i not in marks else i for i in text.split(' ')])