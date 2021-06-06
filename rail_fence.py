import numpy as np

ONE_LETTERS = ['e', 't', 'a', 'o', 'i', 'n', 's', 'h', 'r', 'd', 'l', 'u']
TWO_LETTERS = [
    'th', 'er', 'on', 'an', 're', 'he', 'in', 'ed', 'nd', 'ha', 'at', 
    'en', 'es', 'of' 'or', 'nt', 'ea', 'ti', 'to', 'it', 'st', 'io', 
    'le', 'is', 'ou', 'ar', 'as', 'de', 'rt', 've', 'ss', 'ee', 'tt', 'ff', 'll', 'mm', 'oo'
]
THREE_LETTERS = [
    'the', 'and', 'tha', 'ent', 'ion', 'tio', 'for', 'nde', 'has', 'nce', 'edt', 'tis', 'oft', 'sth', 'men',
    'for', 'are', 'but', 'not', 'you', 'all', 'any', 'can', 'had', 'her', 'was', 'one', 'our', 'out', 'day', 
    'get', 'has', 'him', 'his', 'how', 'man', 'new', 'now', 'old', 'see', 'two', 'way', 'who', 'boy', 'did', 
    'its', 'let', 'put', 'say', 'she', 'too', 'use'
]
FOUR_LETTERS = [
    'that', 'with', 'have', 'this', 'will', 'your', 'from', 
    'they', 'know', 'want', 'been', 'good', 'much', 'some', 'time'
]

# TWO_LETTERS = [
#     ' of ', ' to ', ' in ', ' it ', ' is ', ' be ', ' as ', ' at ', ' so ', 'we ', 'he ', ' by ', ' or ', 
#     ' on ', ' do ', ' if ', ' me', 
#     'my ', 'up ', ' an ', ' go ', ' no ', ' us', ' am'
# ]
# THREE_LETTERS = [
#     'the ', ' and ', ' for', 'are ', 'but ', 'not ', 'you', 'all', 'any ', ' can ', 'had ', 'her ', 'was ', 'one', 
#     'our ', 'out', 'day', 'get ', 'has ', 'him', 'his ', 'how ', 'man', 'new', 'now', 'old', 'see ', 'two', 
#     'way', 'who ', 'boy', 'did ', 'its ', 'let ', 'put ', 'say ', 'she ', 'too', 'use '
# ]
# FOUR_LETTERS = [
#     ' that ', ' with ', ' have ', 'this ', 'will ', 'your ', 'from ', 'they ', 'know', 
#     'want ', ' been', 'good', 'much', 'some', 'time'
# ]

def encrypt(plain_text, key):
    print('encrypt is running ...')
    rails = ['',] * key
    down = True
    curr_id = 0

    for c in plain_text:
        rails[curr_id] += c
        if curr_id == 0:
            down = True
            curr_id += 1
        elif curr_id == key-1:
            curr_id -= 1
            down = False
        else:
            if down:
                curr_id += 1
            else:
                curr_id -= 1
    print(rails)
    return ''.join(rails)

def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))] 
                  for j in range(key)]
    dir_down = None
    row, col = 0, 0
      
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
          
        rail[row][col] = '*'
        col += 1
          
        if dir_down:
            row += 1
        else:
            row -= 1
              
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if ((rail[i][j] == '*') and
               (index < len(cipher))):
                rail[i][j] = cipher[index]
                index += 1
          
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):
          
        if row == 0:
            dir_down = True
        if row == key-1:
            dir_down = False
              
        if (rail[row][col] != '*'):
            result.append(rail[row][col])
            col += 1
              
        if dir_down:
            row += 1
        else:
            row -= 1
    return("".join(result))

def score(plaint_text):
    _score = 0
    plaint_text = str.lower(plaint_text)
    # for i, letter in enumerate(ONE_LETTERS):
    #     _score += plaint_text.count(letter) * ((len(ONE_LETTERS) - i) / len(ONE_LETTERS)) / 4
    
    for i, list_words in enumerate([TWO_LETTERS, THREE_LETTERS, FOUR_LETTERS]):
        for word in list_words:
            _score += plaint_text.count(word) * (i + 2) / 3
    
    return _score

def decrypt_without_key(cipher):
    max_score = 0
    ret = None

    for key in range(2, 100):
        plain_text = decrypt(cipher, key)
        my_score = score(plain_text)
        print('________________________________________________________')
        print('{0}: {1}'.format(plain_text, my_score))
        if my_score > max_score:
            print('better score')
            max_score = my_score
            ret = plain_text
        
    return ret

plain_text = 'Although rail-fence cipher is easy to crack, it is generally used in combination with other ciphers like a substitution cipher to make it safer.'
plain_text = 'Soooo, did you see the Warriors game last night? Crazy, right? It was nice to see Harrison Barnes back and the entire crowd cheered when he entered the game. Steph Curry is probably not human, because he shoots the ball from the parking lot and it swishes like butter. How many characters am I up to now? Lemme check, so hold on….597.'
cipher = encrypt(plain_text, 4)
print(cipher)
print('plaintext true: ', decrypt(cipher, 4))
print('plaintext temp: ', decrypt_without_key(cipher))