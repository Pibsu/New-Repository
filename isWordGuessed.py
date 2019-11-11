"Prog Assignment: func#1"
def isWordGuessed(secretWord,lettersGuessed):
    letcount = 0
    for i,x in enumerate(secretWord):
    	if x in lettersGuessed:
    		letcount +=1
    if letcount == len(secretWord):
    	print(bool(1))
    else:
    	print(bool(0))

