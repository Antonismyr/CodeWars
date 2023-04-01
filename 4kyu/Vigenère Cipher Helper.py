class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet
        self.code = ''
        
    def createLen(self, text):
#         listKey = list(self.key)
        mul = len(text) // len(self.key)
        mod = len(text) % len(self.key)
        return self.key * mul + self.key[:mod]
    
    def encode(self, text):
        self.code = self.createLen(text)
        return ''.join([self.alphabet[(self.alphabet.index(k) + self.alphabet.index(self.code[i]))%len(self.alphabet)] if k in self.alphabet else k for i, k in enumerate(text)])
    
    def decode(self, text):
        self.code = self.createLen(text)
        return ''.join([self.alphabet[(self.alphabet.index(k) - self.alphabet.index(self.code[i]))%len(self.alphabet)] if k in self.alphabet else k for i, k in enumerate(text)])