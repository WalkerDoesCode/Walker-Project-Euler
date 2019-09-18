'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #16
'''

import time

def projectEulerProblemSixteen(m,n):
    a = str(m**n)
    total = 0
    for c in a:
        total+=int(c)
    return total

start = time.time()
print projectEulerProblemSixteen(2, 1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1366
--- 0.000135898590088 seconds ---

for input of m=2, n=1000
'''