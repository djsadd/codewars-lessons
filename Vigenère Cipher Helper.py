class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        password = self.get_str(text)

        word = ''

        for i in range(len(text)):
            if text[i] not in self.alphabet:
                word += text[i]
                continue
            three = self.alphabet.find(text[i]) + self.alphabet.find(password[i])

            word += self.alphabet[three % len(self.alphabet)]
        return word

    def decode(self, text):
        password = self.get_str(text)
        word = ''
        for i in range(len(text)):
            if text[i] not in self.alphabet:
                word += text[i]
                continue
            word += self.alphabet[(self.alphabet.find(text[i])-self.alphabet.find(password[i])) % len(self.alphabet)]

        return word

    def get_str(self, text):
        password = ''
        i = 0
        k = 0
        while len(text) != len(password):
            if k > len(self.key) - 1:
                k = 0

            if text[i] in self.alphabet:
                password += self.key[k]
                k += 1
                i += 1
            else:
                password += text[i]
                i += 1
                k += 1
        return password


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
c = VigenereCipher(key, alphabet)

print(c.encode("it's a shift cipher"))
print(c.decode("xt'k s ovzii cahdsi"))
print(c.decode("xt'k o vwixl qzswej"))