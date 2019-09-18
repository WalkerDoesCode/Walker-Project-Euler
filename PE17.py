'''
Author: Walker Kroubalkian
Library Approach to Project Euler Problem #17
'''

import inflect
import time

def countLetters(myString):
    total = 0
    for c in myString:
        if "a"<=c<="z":
            total+=1
    return total

def projectEulerProblemSeventeen(n):
    total = 0
    i = inflect.engine()
    for x in range(1,(n+1)):
        total+=countLetters(i.number_to_words(x))
    return total

start = time.time()
print projectEulerProblemSeventeen(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

21124
--- 0.0325779914856 seconds ---

for input of n=1000
'''