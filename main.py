from primenums import *
from rankwords import *

def matchWords(target,guess):
    target = list(target)
    guess = list(guess)
    mask = ['x','x','x','x','x']
    for i in range(len(target)):
        if target[i] == guess[i]:
            mask[i]='g'
            target[i] = '-'
    for i in range(len(target)):
        if mask[i] == 'g': continue
        if guess[i] in target:
            mask[i] = 'y'
            for x,l in enumerate(target): 
                if l == guess[i]:
                    target[x] = '-'
                    break
        else:
            mask[i] = 'x'
    return mask


def updateNum(num,all_nums,greys,mask,target,guess):
    for i in range(len(target)):
        if mask[i] == 'g':
            temp_num = numlet[guess[i]]['green'][i]
            if temp_num not in all_nums:
                all_nums.append(temp_num)
                num*= temp_num
        elif mask [i] == 'y':
            temp_num = numlet[guess[i]]['yellow'][i]
            if temp_num not in all_nums:
                all_nums.append(temp_num)
                num*= temp_num
        elif mask[i] == 'x':
            greys.append(guess[i])
    return num,all_nums,greys
    
def findPossible(num,greys):
    possibleWords = []
    for id in list(wordnum.keys()):
        if id%num == 0:
            bad = False
            for p in greys:
                if p in wordnum[id]:
                    bad = True
            if bad == False:      
                possibleWords.append(wordnum[id])
    return possibleWords

def makeGuess(important,target,guess,):
    num,all_nums,greys = important[0], important[1], important[2]
    mask = matchWords(target,guess)
    update_results = updateNum(num,all_nums,greys,mask,target,guess)
    possibleWords = findPossible(update_results[0],update_results[2])
    
    return update_results[0],update_results[1],update_results[2],possibleWords

def attemptWord(target):
    num = 1
    all_nums = []
    greys = []
    correct = False
    info = [num,all_nums,greys,guesslist]
    guessCount = 0
    previousGuesses = []

    while correct != True:
        if len(info[3]) < 50:
            guess = bestPossibleChoice(info[3])[0]
        else:
            guess = mostInfo(previousGuesses,info[3])
        print(guess)
        info = makeGuess(info[:3],target,guess)
        guessCount += 1

        if guess == target:
            correct = True
            print(f"Took {guessCount} guesses to get {target}")
        previousGuesses.append(guess)
    
    
def main():
    attemptWord('crane')
            
    
    
main()