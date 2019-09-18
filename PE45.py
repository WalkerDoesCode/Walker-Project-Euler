'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #45
'''

import time
from math import sqrt
from math import ceil

def isPentagon(p):
    if(p==1):
        return True
    n = int(ceil(sqrt(2*p/3)))
    if(n*(3*n-1)/2 == p):
        return True
    return False

def projectEulerProblemFortyFive(n):
    c = n+1
    while(True):
        if(isPentagon(c*(2*c-1))):
            return c*(2*c-1)
        c+=1
    return "HOW"

start = time.time()
print projectEulerProblemFortyFive(143)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1533776805
--- 0.0135638713837 seconds ---

for input of n = 143
'''