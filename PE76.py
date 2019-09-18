'''
Author: Walker Kroubalkian (Heavily inspired by Project Euler's Solution to Project Euler Problem #31)
Dynamic Approach to Project Euler Problem #76
'''

import time

def projectEulerProblemSeventySix(n):
    numbers = []
    for x in range(1,n):
        numbers.append(x)
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(len(numbers)):
        for j in range(numbers[i], n+1):
            ways[j] = ways[j] + ways[j-numbers[i]]
    return ways[n]

start = time.time()
print projectEulerProblemSeventySix(100)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

190569291
--- 0.000514030456543 seconds ---

for input of n = 100.
'''