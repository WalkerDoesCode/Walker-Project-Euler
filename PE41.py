'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #41
'''

import time
from math import sqrt

def listPermutations(myList):
    if(len(myList)==1):
        return [myList]
    a = myList[0]
    b = listPermutations(myList[1:])
    total = []
    for x in b:
        for c in range(len(x)+1):
            temp = x[0:c]
            temp.append(a)
            temp.extend(x[c:])
            total.append(temp)
    return total

def isPrime(n):
    if(n<=1):
        return False
    if(n<4):
        return True
    if(n%2==0):
        return False
    c = 3
    while(c<=sqrt(n)):
        if(n%c==0):
            return False
        c+=2
    return True

def projectEulerProblemFortyOne(n):
    digits = []
    for x in range(1,n+1):
        digits.append(x)
    allPossible = listPermutations(digits)
    maxFound = 0
    for p in allPossible:
        a = ""
        for x in p:
            a+=str(x)
        b = int(a)
        if(isPrime(b)):
            if(b>maxFound):
                maxFound = b
    return maxFound

start = time.time()
print projectEulerProblemFortyOne(7)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

7652413
--- 0.0887989997864 seconds ---

for input of n = 7
'''