def decode(s):
    decrypted_message = ''
    i = 0
    key = "bdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqHa"

    for char in s:
        i += 1
        if char not in key:
            decrypted_message += char
            continue

        idx = (key.index(char) - i) % 66
        decrypted_message += key[idx]

    return decrypted_message


def decode_two(s):
    alph = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789.,? "
    dec = ''
    for pos, enc_char in enumerate(s):
        pos = 2**(pos+1)
        idx = alph.find(enc_char) + 1
        if idx == 0:  # not in alph
            dec += enc_char
            continue
        # modular multiplicative inverse
        ht = (pow(pos, -1, 67))
        dec += alph[(ht * idx % 67)-1]
    return dec

print(decode_two('atC5kcOuKAr!'))