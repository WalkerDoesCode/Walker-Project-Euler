'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #40
'''

import time
from math import ceil

def calculateChampernowneDigit(n):
    c = 1
    total = 0
    while(n-total>c*9*(10**(c-1))):
        total+=c*9*(10**(c-1))
        c+=1
    n-=total
    numbers = int(ceil(1.0*n/(1.0*c)))
    theNumber = 10**(c-1) + numbers-1
    a = str(theNumber)
    return int(a[((n-1)%c)])

def projectEulerProblemForty(myList):
    total = 1
    for x in myList:
        total*=calculateChampernowneDigit(x)
    return total

start = time.time()
print projectEulerProblemForty([1,10,100,1000,10000,100000,1000000])
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

210
--- 3.88622283936e-05 seconds ---

for input of myList = [1,10,100,1000,10000,100000,1000000]
'''