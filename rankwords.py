from guesslist import guesslist
def findCommonLetters(guessable):
    commonLetters = [{},{},{},{},{},]

    for word in guessable:
        for i,letter in enumerate(word):
            if letter in commonLetters[i]:
                commonLetters[i][letter] += 1
            else:
                commonLetters[i][letter] = 1

    mostCommonLettersBySpace = []
    for i in commonLetters:
        federalism = sorted(i.items(),key=lambda x:x[1],reverse=True)
        tempCommonLetters = [x[0] for x in federalism]
        mostCommonLettersBySpace.append(tempCommonLetters)
    return mostCommonLettersBySpace


def wordScore(word,commonLetters):
    score = 1
    for i,let in enumerate(word):
        if let in commonLetters[i]:
            score *= (commonLetters[i].index(let)+1)
        else: 
            score *= 1000
    score *= 4**(5-len(set(word)))
    return score


def bestPossibleChoice(possible,commonLetters=findCommonLetters(guesslist)):
    wordScores = {}
    for choice in possible:
        wordScores[choice] = wordScore(choice,commonLetters)
    bestGuesses = sorted(wordScores.items(),key=lambda x:x[1])
    return bestGuesses[0]
def mostInfo(alreadyGuessed,possible):
    lettersGuessed = "".join(alreadyGuessed)
    lettersGuessed = set(i for i in lettersGuessed)

    noGreyGuess = []

    for word in guesslist:
        if any(x in lettersGuessed for x in word):
            continue
        else:
            noGreyGuess.append(word)
    if len(noGreyGuess)>0:
        return bestPossibleChoice(noGreyGuess,findCommonLetters(possible))[0]
    else:
        return bestPossibleChoice(possible,findCommonLetters(possible))[0]

    
