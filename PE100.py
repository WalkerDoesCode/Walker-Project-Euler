'''
Author: Walker Kroubalkian
Pell Equation Approach to Project Euler Problem #100
'''

import time

def projectEulerProblemOneHundred(n):
    y = 7
    x = 5
    maxY = 2*n-1
    while(y<=maxY):
        tempX = 2*y+3*x
        tempY = 3*y+4*x
        y = tempY
        x = tempX
    return (x+1)/2

start = time.time()
print projectEulerProblemOneHundred(10**12)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

756872327473
--- 1.12056732178e-05 seconds ---

for input of 10**12.
'''