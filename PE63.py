'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #63
'''

import time
from math import ceil, floor

def projectEulerProblemSixtyThree(n):
    total = 0
    for c in range(1,n+1):
        first = ceil(((10.)**(float(c)-1.))**(1./float(c)))
        second = floor(((10.)**(float(c))-1.)**(1./float(c)))
        first = int(first)
        second = int(second)
        
        for x in range(first,second+1):
            if(len(str(x**c))==c):
                total+=1
        
        if(9**c < 10**(c-1)):
            return total
    return total

start = time.time()
print projectEulerProblemSixtyThree(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

49
--- 9.89437103271e-05 seconds ---

for input of n = 1000.
'''