'''
Author: Walker Kroubalkian
Semi-Dynamic Approach to Project Euler Problem #72
'''

import time
from math import sqrt

def projectEulerProblemSeventyTwo(n):
    totients = [1,1]
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
    total = 0
    for x in range(2,n+1):
        total+=totients[x]
    return total

start = time.time()
print projectEulerProblemSeventyTwo(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

303963552391
--- 2.71775197983 seconds ---

for input of n = 1000000.
'''