import random
import string
WORDLIST_FILENAME = "words.txt"
wordlist = ["ball","apple","game","hangman","kangaroo","rope","line","break","continue","lesson","computer","typing","commands","python","anaconda","words","strings","lists","loops",]
def loadWords():
    print("Loading...")
    print("  ", len(wordlist), " words. Loading Complete.")
    return wordlist
def chooseWord(wordlist):
    return random.choice(wordlist)
secretWord = chooseWord(wordlist)

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
def Hangaroo(secretword):    
    numletters = len(secretWord)
    lettersGuessed = []
    guess = str
    mistakes = 4
    wordGuessed = False
    
    print("Hey! It's me! Hangaroo!")
    print("The word to guess is ", numletters, " letters long.")
    print('------------')
    while mistakes > 0 and mistakes <= 4 and wordGuessed is False:
        if secretWord == getGuessedWord(secretWord, lettersGuessed):
            wordGuessed = True
            break
        print ("You have ",mistakes ," guesses left.")
        print ('Available letters: ',getAvailableLetters(lettersGuessed))
        guess = input('Guess a letter: ').lower()
        if guess in secretWord:
            if guess in lettersGuessed:
                print ("Hey! You got that already!: ",getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                print ("Good job.: ",getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
        else:
            if guess in lettersGuessed:
                print ("Hey! You got that already!: ",getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
            else:
                lettersGuessed.append(guess)
                mistakes -= 1
                print ("Nope bruh. Nothing like that here.: ", getGuessedWord(secretWord, lettersGuessed))
                print ('------------')
    
    if wordGuessed == True:
        print("'Congrats. Guess you won?'")
    elif mistakes == 0:
        print ('Better luck next time bud. The word was ',secretWord)
        
     
            
        
