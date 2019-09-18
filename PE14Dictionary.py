'''
Author: Project Euler with Python Implementation by Walker Kroubalkian
Dictionary Approach to Project Euler Problem #14
'''

import time

def projectEulerProblemFourteen(n):
    longestLength = 0
    longestIndex = -1
    knownIndices = {1: 1}
    
    def indexLength(x):
        if x in knownIndices:
            return knownIndices.get(x)
        if(x%2==0):
            knownIndices[x] = indexLength(x/2)+1
        else:
            knownIndices[x] = indexLength(3*x+1)+1
        return knownIndices[x]
    
    for i in range(n/2,n):
        a = indexLength(i)
        if(a > longestLength):
            longestLength = a
            longestIndex = i
    return longestIndex

start = time.time()
print projectEulerProblemFourteen(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

837799
--- 1.09148907661 seconds ---

for input of n=1000000
'''