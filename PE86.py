'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #86
'''

import time
from math import sqrt

def projectEulerProblemEightySix(n):
    m = 0
    squares = [0]
    t = 1
    upper = 2*int(sqrt(5*n))+1
    while(t<upper):
        squares.append(t*t)
        t+=1
    current = 0
    while(current<n):
        m+=1
        cFactor = squares[m]
        for abSum in range(2,2*m+1):
            v = squares[abSum]+cFactor
            value = binarySearch(squares, v)
            if value>-1:
                for a in range(max(abSum-m,1),abSum/2+1):
                    b = abSum - a
                    if(a<=b):
                        if b<=m:
                            current+=1
                    else:
                        break
    return m

def binarySearch(myList, n):
    lower = 0
    upper = len(myList)-1
    while(lower<upper-1):
        middle = (lower+upper)/2
        v = myList[middle]
        if v>n:
            upper = middle
        elif v<n:
            lower = middle
        else:
            return middle
    if(myList[lower]==n):
        return lower
    if(myList[upper]==n):
        return upper
    return -1

start = time.time()
print projectEulerProblemEightySix(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1818
--- 4.28403687477 seconds ---

for input of n = 1000000.
'''