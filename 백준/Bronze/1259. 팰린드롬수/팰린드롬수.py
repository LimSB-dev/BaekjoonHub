while True:
    word = str(input())
    
    if word == '0':
        break
    
    word_reverse = word[::-1]
    
    if word == word_reverse:
        print('yes')
    else:
        print('no')