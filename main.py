import random


def rotate_letter(letter, n):
    """When encrypted by shifting each letter by N positions, it finds the replacement letter and
     returns the discovered letter back.
    """

    # If it is one of the capital letters in the Latin alphabet,
    if letter.isupper():
        start = ord('A')
        mod = 26
    # If it is one of the lowercase letters in the Latin alphabet,
    elif letter.islower():
        start = ord('a')
        mod = 26
    # If it is a digit,
    elif letter.isdigit():
        start = ord('0')
        mod = 10
    else:
        # If it is none of the above,
        return ""

    c = ord(letter) - start
    i = (c + n) % mod + start
    return chr(i)


def vernam_cipher_word(word, keyphrase):
    """It shifts the given word by the given keyphrase amount, essentially implementing Vernam encryption.
    """

    res = ''
    for i in range(len(word)):
        if keyphrase[i].isupper():
            n = ord(keyphrase[i]) - ord('A') + 1
        else:
            n = ord(keyphrase[i]) - ord('a') + 1
        res += rotate_letter(word[i], n)
    return res


def vernam_decipher_word(word, keyphrase):
    """This encrypted word can be deciphered by shifting it back by the length of the keyphrase,
     similar to Vernam decryption.
    """
    res = ''
    for i in range(len(word)):
        if keyphrase[i].isupper():
            n = ord(keyphrase[i]) - ord('A') + 1
        else:
            n = ord(keyphrase[i]) - ord('a') + 1
        res += rotate_letter(word[i], -n)
    return res


def generate_key(n):
    """It generates a random key word of length n. Each letter in the random word has a 50% probability of being
     uppercase and a 50% probability of being lowercase. There are no numbers in the random word.
    """
    key = ""
    lower_start = ord('a')
    upper_start = ord('A')
    for i in range(n):
        # Generate a random letter from the alphabet.
        c = random.randint(0, 25)
        # Either uppercase or lowercase.
        k = random.randint(0, 1)
        if k:
            char = lower_start + c
        else:
            char = upper_start + c
        key = key + chr(char)
    return key


if __name__ == '__main__':
    print("MEETINGplaceBELGIUM")
    keyphrase = generate_key(len("MEETINGplaceBELGIUM"))
    print(keyphrase)
    cipherText = vernam_cipher_word('MEETINGplaceBELGIUM', keyphrase)
    print(cipherText)
    print(vernam_decipher_word(cipherText, keyphrase))
    print("arriveby10oclock")
    keyphrase = generate_key(len("arriveby10oclock"))
    print(keyphrase)
    cipherText = vernam_cipher_word('arriveby10oclock', keyphrase)
    print(cipherText)
    print(vernam_decipher_word(cipherText, keyphrase))
