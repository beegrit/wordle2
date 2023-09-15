from primenums import *







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
    
    
    
def main():
    num = 1
    all_nums = []
    greys = []
    target = "water"
    guess = "crane"
    g = makeGuess([num,all_nums,greys],target,guess)
    g = makeGuess(g[:3],target,"saker")
    g = makeGuess(g[:3],target,"wader")
    
    print((g[3]))


main()