for word in [ 'ox', 'cat', 'lion', 'tiger', 'bobcat' ]:
    for i in range(2,7):
        letters = len(word)
        #print('letters: ', letters)
        if ( letters % i ) == 0:
            print(i, word)


