'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #49
'''

import time

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

def equivalentString(a,b):
    aList = []
    bList = []
    a = str(a)
    b = str(b)
    for x in a:
        aList.append(x)
    for x in b:
        bList.append(x)
    return sorted(aList) == sorted(bList)

def projectEulerProblemFortyNine():
    allPrimes = sieveEratosthenes(10000)
    fourDigit = []
    for x in allPrimes:
        if x>1000:
            fourDigit.append(x)
    
    allTriples = []
    
    l = len(fourDigit)
    for a in range(l):
        for b in range(a+1, l):
            v1 = fourDigit[a]
            v2 = fourDigit[b]
            v3 = (v1+v2)/2
            if v3 in fourDigit:
                if equivalentString(v1, v2) and equivalentString(v1, v3):
                    allTriples.append(sorted([v1,v2,v3]))
    
    final = []
    for x in allTriples:
        s = ""
        for y in x:
            s+=str(y)
        final.append(s)
    
    return final

start = time.time()
print projectEulerProblemFortyNine()
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

['148748178147', '296962999629']
--- 5.9415140152 seconds ---

for no input
'''