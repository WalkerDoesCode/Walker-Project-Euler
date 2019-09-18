'''
Author: Walker Kroubalkian
Combinatorial Approach to Project Euler Problem #15
'''

import time

def projectEulerProblemFifteen(r, c):
    total = 1
    for i in range(1,(c+1)):
        total*=(r+c+1-i)
        total/=i
    return total

start = time.time()
print projectEulerProblemFifteen(20, 20)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

137846528820
--- 1.50203704834e-05 seconds ---

for input of r = 20, c = 20
'''