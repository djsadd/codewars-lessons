class VigenereCipher(object):
    def __init__(self, key, alphabet):
        self.key = key
        self.alphabet = alphabet

    def encode(self, text):
        encypted = []
        alphabet = self.alphabet
        key = self.key
        alphabet_len = len(alphabet)
        key_len = len(key)
        for i, char in enumerate(text):
            encypted.append(alphabet[(alphabet.index(char) + alphabet.index(
                key[i % key_len])) % alphabet_len] if char in alphabet else char)
        return ''.join(encypted)

    def decode(self, text):
        encypted = []
        key = self.key
        key_len = len(key)
        alphabet = self.alphabet
        for i, char in enumerate(text):
            encypted.append(
                alphabet[(alphabet.index(char) - alphabet.index(key[i % key_len]))] if char in alphabet else char)
        return ''.join(encypted)

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
        return password


alphabet = 'abcdefghijklmnopqrstuvwxyz'
key = 'password'

# // creates a cipher helper with each letter substituted
# // by the corresponding character in the key
c = VigenereCipher(key, alphabet)

print(c.encode("it's a shift cipher"))
print(c.decode("xt'k s ovzii cahdsi"))
print(c.decode("xt'k o vwixl qzswej"))