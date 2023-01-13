from string import ascii_lowercase


def add_to_dict(word, di):
    if len(word) != 0 and any(list(map(lambda x: x in ascii_lowercase, word))):
        if word in di:
            di[word] += 1
        else:
            di[word] = 0


def top_3_words(text):
    lst_words = text.split()
    di = {}
    for row in lst_words:
        word = ''
        for res in row:
            lower_word = res.lower()
            if lower_word not in ascii_lowercase+"'":
                add_to_dict(word, di)
                word = ''
                continue

            word += lower_word

        add_to_dict(word, di)
    return list(map(lambda x: x[0], sorted(di.items(), key=lambda x: x[1], reverse=True)))[:3]
