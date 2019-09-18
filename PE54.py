'''
Author: Walker Kroubalkian
Library Approach to Project Euler Problem #54
'''

import time
import eval7

f = open("PE54Hands.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(map(str,x.split()))
else:
    raise ValueError("Cannot read from file")

finalList = realContents

def projectEulerProblemFiftyFour(myList):
    total = 0
    for x in myList:
        a = x[0:5]
        b = x[5:]
        oneHand = []
        for card in a:
            oneHand.append(eval7.Card(card[0]+card[1].lower()))
        twoHand = []
        for card in b:
            twoHand.append(eval7.Card(card[0]+card[1].lower()))
        if(eval7.evaluate(oneHand)>eval7.evaluate(twoHand)):
            total+=1
    return total

start = time.time()
print projectEulerProblemFiftyFour(finalList)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

376
--- 0.00889301300049 seconds ---

for input of finalList = given list of hands.
'''