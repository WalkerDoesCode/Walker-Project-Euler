'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #24
'''

import time

def factorial(n):
    total = 1
    for c in range(2,n+1):
        total*=c
    return total

def projectEulerProblemTwentyFour(n, x):
    myFactorials = []
    for i in range(x):
        myFactorials.append(factorial(x-1-i))
    
    myString = ""
    n-=1
    counter = 0
    
    possibleDigits = []
    for i in range(x):
        possibleDigits.append(str(i))
    
    while(counter<x and len(possibleDigits)>1):
        total = 0
        thisDigit = -1
        while(total<=n):
            total+=myFactorials[counter]
            thisDigit+=1
        myString += possibleDigits[thisDigit]
        n-=(total-myFactorials[counter])
        possibleDigits.pop(thisDigit)
        counter+=1
    
    myString+=possibleDigits[0]
    return myString

start = time.time()
print projectEulerProblemTwentyFour(1000000, 10)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

2783915460
--- 2.90870666504e-05 seconds ---

for input of n = 1000000, x = 10
'''