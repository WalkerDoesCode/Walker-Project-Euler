'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #52
'''

import time

def enumerateString(a):
    aChars = []
    aNums = []
    for x in a:
        if x not in aChars:
            aChars.append(x)
            aNums.append([x,1])
        else:
            aNums[aChars.index(x)][1]+=1
    return aNums

def isPermutation(a,b):
    return sorted(enumerateString(str(a))) == sorted(enumerateString(str(b)))

def projectEulerProblemFiftyTwo(n):
    c = 1
    found = 0
    current = -1
    while(found<n):
        none = False
        for x in range(2,7):
            if(not isPermutation(c,x*c)):
                none = True
                break
        if not none:
            found+=1
            current = c
        c+=1
    return current

start = time.time()
print projectEulerProblemFiftyTwo(1)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

142857
--- 0.808156967163 seconds ---

for input of n = 1.
'''