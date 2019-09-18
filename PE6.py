'''
Author: Walker Kroubalkian
Formulaic Approach to Project Euler Problem #6
'''

import time

def projectEulerProblemSix(n):
    return n*n*(n+1)*(n+1)/4 - n*(n+1)*(2*n+1)/6

start = time.time()
print projectEulerProblemSix(100)
print ("--- %s seconds ---" % (time.time() - start))

'''
Prints

25164150
--- 8.82148742676e-06 seconds ---

for input of n = 100
'''