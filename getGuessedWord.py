def getGuessedWord(secretWord, lettersGuessed):
    letcount = 0
    null = ['_'] * len(secretWord)

    for i, x in enumerate(secretWord):
        if x in lettersGuessed:
            letcount += 1
            null.insert(letcount - 1,x)
            null.pop(letcount)
            if letcount == len(secretWord):
                return ''.join(str(y) for y in null)
        else:
            letcount += 1
            null.insert(letcount-1,'_')
            null.pop(letcount)
            if letcount == len(secretWord):
                return ''.join(str(y) for y in null)