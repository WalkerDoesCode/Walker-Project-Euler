'''
Author: Walker Kroubalkian
Dynamic Approach to Project Euler Problem #77
'''

import time

def subProblem(n,m):
    numbers = sieveEratosthenes(n)
    ways = [0]*(n+1)
    ways[0] = 1
    for i in range(len(numbers)):
        for j in range(numbers[i], n+1):
            ways[j] = ways[j] + ways[j-numbers[i]]
    for x in range(n+1):
        if(ways[x]>m):
            return x
    return -1

def sieveEratosthenes(n):
    myPrimes = []
    
    primePossible = [True]*(n+1)
    primePossible[0] = False
    primePossible[1] = False
    
    for (i,possible) in enumerate(primePossible):
        if possible:
            for x in range(i*i, (n+1), i):
                primePossible[x] = False
            myPrimes.append(i)

    return myPrimes

def projectEulerProblemSeventySeven(m):
    c = 10
    while(True):
        a = subProblem(c, m)
        if(a!=-1):
            return a
        c*=3

start = time.time()
print projectEulerProblemSeventySeven(5000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

71
--- 0.000175952911377 seconds ---

for input of m = 5000.
'''