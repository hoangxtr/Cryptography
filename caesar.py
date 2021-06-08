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

def score1(plaint_text):
    _score = 0
    plaint_text = str.lower(plaint_text)
    for i, letter in enumerate(ONE_LETTERS):
        _score += plaint_text.count(letter) * ((len(ONE_LETTERS) - i) / len(ONE_LETTERS)) / 4
    
    for i, list_words in enumerate([TWO_LETTERS, THREE_LETTERS, FOUR_LETTERS]):
        for word in list_words:
            _score += plaint_text.count(word) * (i + 2) / 4
    
    return _score

def score2(plaint_text):
    _score = 0
    plaint_text = str.lower(plaint_text)
    # for i, letter in enumerate(ONE_LETTERS):
    #     _score += plaint_text.count(letter) * ((len(ONE_LETTERS) - i) / len(ONE_LETTERS)) / 4
    
    for i, list_words in enumerate([TWO_LETTERS, THREE_LETTERS, FOUR_LETTERS]):
        for word in list_words:
            _score += plaint_text.count(word) * (i + 1) / 3
    
    return _score

def decrypt_without_key(cipher):
    ret = {}
    rets = []
    plaintexts = []
    scores = []
    for key in range(26):
        plaintext = decrypt(cipher, key)
        plaintexts.append(plaintext)
        _score = score2(plaintexts[-1])
        scores.append(_score)
        rets.append({'key': key, 'score': _score, 'plaintext': plaintext})

    # print(rets)
    rets = sorted(rets, key=lambda d: d['score'], reverse=True)
    print('Decode with Caesar with score:')
    for i in range(len(rets)):
        print('{0}'.format(rets[i]))
    print('Candidate max: {0}'.format(plaintexts[np.argmax(scores)]))
    return rets[0]
    



plaintext = 'I am a student at Ho Chi Minh University of Technology'.lower()
cipher = encrypt(plaintext, ord('a') - ord('s') + 26)
print('Cipher: {0}\n'.format(cipher))

print(decrypt_without_key(cipher))