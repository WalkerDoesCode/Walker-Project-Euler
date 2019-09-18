'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #62
'''

import time

def isPermutation(a,b):
    c = str(a)
    d = str(b)
    if(len(c)!=len(d)):
        return False
    return sorted(c) == sorted(d)

def projectEulerProblemSixtyTwo(n):
    c = 345
    found = 0
    current = -1
    cubes = []
    currCube = c**3
    while(found<n):
        c+=1
        v = c**3
        if(len(str(v))>len(str(currCube))):
            cubes = []
        currCube = v
        t = 0
        first = -1
        for a in cubes:
            if isPermutation(a,currCube):
                if(first==-1):
                    first = a
                t+=1
        if(t==4):
            found+=1
            current = first
        cubes.append(currCube)
    return current

start = time.time()
print projectEulerProblemSixtyTwo(1)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

127035954683
--- 21.7080910206 seconds ---

for input of n = 1.
'''