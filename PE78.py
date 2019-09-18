'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #78
'''

import time

def subProblem(n,x):
    numbers = []
    for y in range(1,n+1):
        numbers.append(y)
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(len(numbers)):
        for j in range(numbers[i], n+1):
            ways[j] = (ways[j] + ways[j-numbers[i]])%x
    for y in range(n+1):
        if (ways[y])%x == 0:
            return y
    return -1

def projectEulerProblemSeventyEight(n):
    c = 10
    while True:
        a = subProblem(c,n)
        if(a!=-1):
            return a
        c*=3
        

start = time.time()
print projectEulerProblemSeventyEight(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

55374
--- 222.313875198 seconds ---

for input of n = 1000000.
'''