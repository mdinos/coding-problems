def is_pangram(sentence):
    sentence = sentence.lower()
    alphabet = 'abcdefghijklmopqrstuvwxyz'
    for a in alphabet:
        if a in sentence:
            continue
        else:
            return False
    return True