class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):

        word = ''

        for i in range(len(text)):
            if text[i] not in self.alphabet:
                word += text[i]
                continue
            three = self.alphabet.find(text[i]) + self.alphabet.find(self.key[i % len(self.key)])

            word += self.alphabet[three % len(self.alphabet)]
        return word

    def decode(self, text):
        word = ''
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                word += text[i]
                continue
            word += self.alphabet[(self.alphabet.find(text[i])-self.alphabet.find(self.key[i % len(self.key)])) % len(self.alphabet)]

        return word


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
c = VigenereCipher(key, alphabet)

print(c.encode("it's a shift cipher"))
print(c.decode("xt'k s ovzii cahdsi"))
print(c.decode("xt'k o vwixl qzswej"))