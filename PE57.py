'''
Author: Walker Kroubalkian
Pell Equation Approach to Project Euler Problem #57
'''

import time

def projectEulerProblemFiftySeven(n):
    numerator = 1
    denominator = 1
    total = 0
    for x in range(n):
        numerator+=2*denominator
        denominator = numerator - denominator
        if(len(str(numerator))>len(str(denominator))):
            total+=1
    return total

start = time.time()
print projectEulerProblemFiftySeven(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

153
--- 0.00200414657593 seconds ---

for input of n = 1000.
'''