class VigenereCipher(object):
    def __init__(self, key: str, alphabet: str):
        self.alphabet = list(alphabet)
        self.key = [alphabet.index(i) for i in key]

    def encode(self, text):
        return "".join([self.alphabet[(self.alphabet.index(text[i]) + self.key[i % len(self.key)]) % len(self.alphabet)]
                        if text[i] in self.alphabet else text[i] for i in range(len(text))])

    def decode(self, text):
        return "".join([self.alphabet[(self.alphabet.index(text[i]) - self.key[i % len(self.key)]) % len(self.alphabet)]
                        if text[i] in self.alphabet else text[i] for i in range(len(text))])


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
c = VigenereCipher(key, alphabet)

print(c.encode("it's a shift cipher"))
print(c.decode("xt'k s ovzii cahdsi"))
print(c.decode("xt'k o vwixl qzswej"))