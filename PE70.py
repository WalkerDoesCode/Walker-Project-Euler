'''
Author: Walker Kroubalkian
Semi-Dynamic Approach to Project Euler Problem #70
'''

import time
from math import sqrt

def isPermutation(a,b):
    return sorted(str(a)) == sorted(str(b))

def projectEulerProblemSeventy(n):
    totients = [1,1]
    minNumerator = -1
    minDenominator = 1
    
    for x in range(2,n+1):
        v = -1
        if(x%2==0):
            if(x%4==0):
                v = totients[x/2]*2
            else:
                v = totients[x/2]
        else:
            c = 3
            myRoot = sqrt(x)
            while(c<=myRoot):
                if(x%c==0):
                    if(x%(c*c)==0):
                        v = totients[x/c]*c
                    else:
                        v = totients[x/c]*(c-1)
                    break
                c+=2
            if(c>myRoot):
                v = x-1
        totients.append(v)
        if(x%9==v%9):
            if(isPermutation(x, v)):
                if(minNumerator == -1):
                    minNumerator = x
                    minDenominator = v
                elif(minNumerator*v>minDenominator*x):
                    minNumerator = x
                    minDenominator = v
    return minNumerator

start = time.time()
print projectEulerProblemSeventy(10000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

8319823
--- 66.285148859 seconds ---

for input of n = 10000000
'''