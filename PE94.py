'''
Author: Walker Kroubalkian
Pell Equation Approach to Project Euler Problem #94
'''

import time

def projectEulerProblemNinetyFour(n):
    # l, l, l+1 Triangles
    y = 14
    x = 8
    pTotal = 0
    while(y<=n-2):
        pTotal+=(y+2)
        yTemp = 7*y+12*x
        xTemp = 4*y+7*x
        y = yTemp
        x = xTemp
    y = 52
    x = 30
    while(y<=n+2):
        pTotal+=(y-2)
        yTemp = 7*y+12*x
        xTemp = 4*y+7*x
        y = yTemp
        x = xTemp
    return pTotal

start = time.time()
print projectEulerProblemNinetyFour(10**9)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints



for input of n = 10**9.
'''