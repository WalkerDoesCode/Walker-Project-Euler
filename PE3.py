'''
Author: Walker Kroubalkian
"Dividing Out" Approach to Project Euler Problem #3
'''

import time
from math import sqrt

def projectEulerProblemThree(n):
    c = 2
    while(c<=sqrt(n)):
        if(n%c==0):
            while(n%c==0):
                n/=c
        c+=1
    if(n==1):
        return (c-1)
    return n

start = time.time()
print projectEulerProblemThree(600851475143)
print("--- %s seconds ---" % (time.time() - start))

'''
Prints

6857
--- 0.00019097328186 seconds ---

for input of n = 600851475143
'''