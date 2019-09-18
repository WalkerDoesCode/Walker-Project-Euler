'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #60
'''

import time
from math import sqrt

def isPrime(n):
    if(n%2==0):
        return False
    c = 3
    while(c<=sqrt(n)):
        if(n%c==0):
            return False
        c+=2
    return True

def concatenatePrime(a,b):
    p1 = int(str(a)+str(b))
    if not isPrime(p1):
        return False
    return isPrime(int(str(b)+str(a)))

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

def subsets(myList,n):
    a = myList[0]
    l = len(myList)
    if(n>l):
        return []
    if(n==l):
        return [myList]
    if(n==0):
        return [[]]
    first = subsets(myList[1:],n-1)
    total = subsets(myList[1:],n)
    for x in first:
        c = x[:]
        c.append(a)
        total.append(sorted(c))
    return total


    

def projectEulerProblemSixty(n):
    consideredPrimes = []
    primeConcats = []
    c = 3
    found = 0
    indexCheck = subsets([0,1,2,3],2)
    current = [-1]
    minSum = -1
    while(found<n):
        if(isPrime(c)):
            if c not in consideredPrimes:
                concatPossible = []
                l = len(consideredPrimes)
                for a in range(l):
                    if(concatenatePrime(consideredPrimes[a], c)):
                        concatPossible.append(a)
                        primeConcats[a].append(l)
                if(len(concatPossible)>=4):       
                    toCheck = subsets(concatPossible,4)
                    for a in toCheck:
                        haveFound = False
                        for b in indexCheck:
                            x = b[0]
                            y = b[1]
                            if a[x] not in primeConcats[a[y]]:
                                haveFound = True
                                break
                        if not haveFound:
                            found+=1
                            e = [c]
                            for z in a:
                                e.append(consideredPrimes[z])
                            subTotal = 0
                            for t in e:
                                subTotal+=t
                            if(current!=[-1]):
                                if(subTotal<minSum):
                                    current = e
                                    minSum = subTotal
                            else:
                                current = e
                                minSum = subTotal
                                
                consideredPrimes.append(c)
                primeConcats.append(concatPossible)
        c+=2
    return minSum

start = time.time()
print projectEulerProblemSixty(1)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

26033
--- 30.2959289551 seconds ---

for input of n = 1.
'''
