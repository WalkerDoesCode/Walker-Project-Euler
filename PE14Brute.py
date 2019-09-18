'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #14
'''

import time

def getCollatzLength(x):
    t = 0
    while(x>1):
        if(x%2==0):
            x/=2
        else:
            x = 3*x+1
        t+=1
    return t

def projectEulerProblemFourteen(x):
    maxIndex = -1
    maxLength = 0
    for i in range(1,x):
        a = getCollatzLength(i)
        if(a>maxLength):
            maxLength = a
            maxIndex = i
    return maxIndex

start = time.time()
print projectEulerProblemFourteen(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

837799
--- 11.196969986 seconds ---

for input of n=1000000
'''