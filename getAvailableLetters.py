def getAvailableLetters(lettersGuessed):
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    lettersRemain = alphabet[:]

    def removeGuessed(x, y):
        x1 = x[:]
        for z in x:
            if z in x1:
                y.remove(z)
        return(''.join(str(z) for z in y))
    print(removeGuessed(lettersGuessed, lettersRemain))