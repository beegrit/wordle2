from primenums import *
from rankwords import *

def matchWords(target,guess,liw):
    target = list(target)
    guess = list(guess)
    mask = ['x','x','x','x','x']
    for i in range(len(target)):
        if target[i] == guess[i]:
            if guess[i] not in liw: liw.append(guess[i])
            mask[i]='g'
            target[i] = '-'
    for i in range(len(target)):
        if mask[i] == 'g': continue
        if guess[i] in target:
            if guess[i] not in liw: liw.append(guess[i])
            mask[i] = 'y'
            for x,l in enumerate(target): 
                if l == guess[i]:
                    target[x] = '-'
                    break
        else:
            mask[i] = 'x'
    return mask,liw


def updateNum(num,all_nums,greys,mask,target,guess,liw):
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
            if guess[i] not in liw:
                for j in greys:
                    j.append(guess[i])
            else:
                greys[i].append(guess[i])
    return num,all_nums,greys
    
def findPossible(num,greys):
    possibleWords = []
    for id in list(wordnum.keys()):
        if id%num == 0:
            bad = False
            for x,let in enumerate(wordnum[id]):
                if let in greys[x]:
                    bad = True  
                    break
            if bad == False:      
                possibleWords.append(wordnum[id])
    return possibleWords

def makeGuess(important,target,guess,liw):
    num,all_nums,greys = important[0], important[1], important[2]
    mask = matchWords(target,guess,liw)
    update_results = updateNum(num,all_nums,greys,mask[0],target,guess,liw)
    possibleWords = findPossible(update_results[0],update_results[2])
    
    return update_results[0],update_results[1],update_results[2],possibleWords

def attemptWord(target,debug=False):
    num = 1
    all_nums = []
    greys = [[] for x in range(5)]
    correct = False
    info = [num,all_nums,greys,guesslist]
    guessCount = 0
    previousGuesses = []
    lettersInWord = []
    
    while correct != True:
        
        if len(info[3]) < 10:
            guess = bestPossibleChoice(info[3],commonLetters=findCommonLetters(info[3]))[0]
        else:
            guess = mostInfo(previousGuesses,info[3])
        if debug == True: 
            print(guess)
            # possible_letters = "".join(info[3])
            # possible_letters = set(i for i in possible_letters)
            # print(len(info[3])/len(possible_letters))
            
        info = makeGuess(info[:3],target,guess,lettersInWord)
        guessCount += 1
        
        if guess == target:
            correct = True
            if debug == True: print(guessCount)
            return guessCount
        previousGuesses.append(guess)
    
def first1000Avg():
    totalGuesses = 0
    wordGuesses = {}
    for i,word in enumerate(guesslist[:1000]):
        guessCount = attemptWord(word)
        wordGuesses[word] = guessCount
        totalGuesses+=guessCount
        print(f'{word} took {guessCount} guesses --- Avg: {round(totalGuesses/(i+1),2)}')
        
        #1st avg 5.57 - 9-20-23 11:40pm - 1000
        #2nd avg 4.37 - 9-21-23 12:40am - 1000
        #3rd avg 4.15 - 9-21-23 12:55am - 1000
        #4th avg 4.05 - 9-21-23 1:32am - 1000
        #5th avg 4.03 - 9-21-23 10:00pm - 1000
        #6th avg 3.91 - 9-21-23 10:20pm - 1000
        #7th avg 3.87 - 9-21-23 10:38pm - 1000
        #8th avg 3.86 - 9-21-23 10:45pm - 1000
        
    print(sorted(wordGuesses.items(), key=lambda x:x[1],reverse=True))
def main():
    first1000Avg()
    #attemptWord('dimes',debug=True)
            
    
    
main()