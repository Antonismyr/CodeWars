import re
from collections import Counter

def top_3_words(text):
    splitText = re.findall('\'*[a-z][a-z\']*', text.lower())
    return [i for i,k in Counter(splitText).most_common(3)]