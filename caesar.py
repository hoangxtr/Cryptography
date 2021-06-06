import numpy as np

ONE_LETTERS = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
TWO_LETTERS = [
    'th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 
    'en', 'es', 'of' 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 
    'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've', 'ss', 'ee', 'tt', 'ff', 'll', 'mm', 'oo'
]
THREE_LETTERS = [
    'the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men'
]
FOUR_LETTERS = [
    'that', 'with', 'have', 'this', 'will', 'your', 'from', 
    'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time'
]


def decrypt(cipher, key):
    plaintext = ''
    for i in cipher:
        plaintext += chr((ord(i) + key - ord('a')) % 26 + ord('a')) 
    return plaintext

def encrypt(plaint_text, key):
    FIRST = ord('a')
    END = ord('z')
    cipher = ''
    for c in plaint_text:
        if ord(c) > END or ord(c) < FIRST:
            continue
        cipher += chr((ord(c) - FIRST + key) % 26 + FIRST)
    
    return cipher

def score(plaint_text):
    _score = 0
    plaint_text = str.lower(plaint_text)
    for i, letter in enumerate(ONE_LETTERS):
        _score += plaint_text.count(letter) * ((len(ONE_LETTERS) - i) / len(ONE_LETTERS)) / 4
    
    for i, list_words in enumerate([TWO_LETTERS, THREE_LETTERS, FOUR_LETTERS]):
        for word in list_words:
            _score += plaint_text.count(word) * (i + 2) / 4
    
    return _score

def decrypt_without_key(cipher):
    plaintexts = []
    scores = []
    for key in range(1, 26):
        plaintext = decrypt(cipher, key)
        plaintexts.append(plaintext)
        scores.append(score(plaintexts[-1]))
        print('\n{0}:{1}'.format(plaintext, scores[-1]))
    print('Cipher max: \n{0}'.format(plaintexts[np.argmax(scores)]))
    



plaintext = 'Note that, in some cases, effort can be shared between ciphers. For example, the Vigenère and autokey ciphers are identical for the beginning of the message; they only start to behave differently when the end of the keyword is reached. It may also be a good idea to try simple variants of these ciphers, such as switching the encryption and decryption rules around; some of them work equally well in both directions, and may have been used so.'.lower()
cipher = encrypt(plaintext, ord('a') - ord('s') + 26)
print('cipher: ', cipher)

decrypt_without_key(cipher)