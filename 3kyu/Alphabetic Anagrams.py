import math 
def listPosition(word):
    """Return the anagram list position of the word"""
    idx = 0
    while len(word):
        possComb = math.factorial(len(word))
        uniqLetters = sorted(list(set(word)))
        for i in uniqLetters:
            possComb = possComb // math.factorial(word.count(i))
        for i in uniqLetters:
            if i < word[0]:
                idx += possComb // len(word) * word.count(i)
        word = word[1:]
    return int(idx+1)