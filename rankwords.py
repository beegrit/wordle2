from guesslist import guesslist

commonLetters = [{},{},{},{},{},]

for word in guesslist:
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


def wordScore(word):
    score = 1
    for i,let in enumerate(word):
        score *= (mostCommonLettersBySpace[i].index(let)+1)
    score *= 4**(5-len(set(word)))
    return score


def bestPossibleChoice(possible):
    wordScores = {}
    for choice in possible:
        wordScores[choice] = wordScore(choice)
    bestGuesses = sorted(wordScores.items(),key=lambda x:x[1])
    return bestGuesses[0]
def mostInfo(alreadyGuessed):
    lettersGuessed = "".join(alreadyGuessed)
    lettersGuessed = set(i for i in lettersGuessed)

    noGreyGuess = []

    for word in guesslist:
        if any(x in lettersGuessed for x in word):
            continue
        else:
            noGreyGuess.append(word)

    return bestPossibleChoice(noGreyGuess)[0]

    
