'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #51
'''

import time
from math import sqrt

def listSubsets(myList,n):
    l = len(myList)
    if(l<n):
        return []
    if(n==0):
        return [[]]
    a = myList[0]
    first = listSubsets(myList[1:],n)
    second = listSubsets(myList[1:],n-1)
    total = first[:]
    for b in second:
        c = b[:]
        c.append(a)
        total.append(sorted(c))
    return total

def primePossibilities(x):
    a = str(x)
    l = len(a)
    possibilities = []
    twos = []
    ones = []
    zeros = []
    for y in range(l):
        v = int(a[y])
        if(v==2):
            twos.append(y)
        elif(v==1):
            ones.append(y)
        elif(v==0):
            zeros.append(y)
    zeroTriples = listSubsets(zeros, 3)
    oneTriples = listSubsets(ones, 3)
    twoTriples = listSubsets(twos, 3)
    for triple in zeroTriples:
        firstIndex = triple[0]
        secondIndex = triple[1]
        thirdIndex = triple[2]
        total = [x]
        for c in range(1,10):
            letter = str(c)
            total.append(int(a[0:firstIndex] + letter+ a[firstIndex+1:secondIndex]+letter + a[secondIndex+1:thirdIndex]+letter+a[thirdIndex+1:]))
        possibilities.append(total)
    for triple in oneTriples:
        firstIndex = triple[0]
        secondIndex = triple[1]
        thirdIndex = triple[2]
        total = [x]
        for c in range(2,10):
            letter = str(c)
            total.append(int(a[0:firstIndex] + letter+ a[firstIndex+1:secondIndex]+letter + a[secondIndex+1:thirdIndex]+letter+a[thirdIndex+1:]))
        possibilities.append(total)
    for triple in twoTriples:
        firstIndex = triple[0]
        secondIndex = triple[1]
        thirdIndex = triple[2]
        total = [x]
        for c in range(3,10):
            letter = str(c)
            total.append(int(a[0:firstIndex] + letter+ a[firstIndex+1:secondIndex]+letter + a[secondIndex+1:thirdIndex]+letter+a[thirdIndex+1:]))
        possibilities.append(total)
    return possibilities

def isPrime(n):
    if(n<=1):
        return False
    if(n<4):
        return True
    if(n%2==0):
        return False
    c=3
    while(c<=sqrt(n)):
        if(n%c==0):
            return False
        c+=2
    return True

def projectEulerProblemFiftyOne(n):
    found = 0
    possible = 3
    current = -1
    while(found<n):
        if(isPrime(possible)):
            a = primePossibilities(possible)
            for replaced in a:
                total = 0
                for x in replaced:
                    if isPrime(x):
                        total+=1
                if(total>=8):
                    current = possible
                    found+=1
        possible+=2
    return current

start = time.time()
print projectEulerProblemFiftyOne(1)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

121313
--- 0.314001083374 seconds ---

for input of n=1
'''