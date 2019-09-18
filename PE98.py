'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #98
'''

import time
from math import sqrt

f = open("PE98Words.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(x.split(","))
else:
    raise ValueError("Cannot read from file")

finalContents = realContents[0]
goodContents = []
for x in finalContents:
    goodContents.append(x[1:len(x)-1])

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

def isAnagram(a,b):
    return sorted(a) == sorted(b)

def subset(myList,n):
    l = len(myList)
    if(l==0):
        if(n==0):
            return [[]]
        return []
    if(l<n):
        return []
    if(l==n):
        return [sorted(myList)]
    a = myList[0]
    total = subset(myList[1:],n)
    possible = subset(myList[1:],n-1)
    for x in possible:
        t = x[:]
        t.append(a)
        total.append(sorted(t))
    return total

def permutations(myList):
    l = len(myList)
    if(l==0):
        return []
    if(l==1):
        return [myList]
    a = myList[0]
    b = permutations(myList[1:])
    total = []
    for c in b:
        for x in range(l):
            t = c[0:x]
            t.append(a)
            t.extend(c[x:])
            total.append(t)
    return total

def isSquare(n):
    a = int(sqrt(n))
    if(a*a==n):
        return True
    return False

def getOtherNumber(myPair, myNumber):
    a = myPair[0]
    b = myPair[1]
    la = []
    ia = []
    lb = []
    ib = []
    for x in range(len(a)):
        l = a[x]
        if l in la:
            ia[la.index(l)].append(x)
        else:
            la.append(l)
            ia.append([x])
    for x in range(len(b)):
        l = b[x]
        if l in lb:
            ib[lb.index(l)].append(x)
        else:
            lb.append(l)
            ib.append([x])
    aFirst = True
    foundA = []
    for x in range(len(la)):
        v = myNumber[ia[x][0]]
        if v in foundA:
            aFirst = False
            break
        else:
            foundA.append(v)
        for z in ia[x]:
            if myNumber[z]!=v:
                aFirst = False
                break
        if not aFirst:
            break
    bFirst = True
    foundB = []
    for x in range(len(lb)):
        v = myNumber[ib[x][0]]
        if v in foundB:
            bFirst = False
            break
        else:
            foundB.append(v)
        for z in ib[x]:
            if myNumber[z]!=v:
                bFirst = False
                break
        if not bFirst:
            break
    if not aFirst and not bFirst:
        return False
    final = []
    if aFirst:
        t = " "*len(a)
        for x in range(len(la)):
            v = foundA[x]
            for n in ib[lb.index(la[x])]:
                t = t[0:n] + v + t[n+1:]
        final.append(t)
    if bFirst:
        t = " "*len(a)
        for x in range(len(lb)):
            v = foundB[x]
            for n in ia[la.index(lb[x])]:
                t = t[0:n] + v + t[n+1:]
        final.append(t)
    return final

def projectEulerProblemNinetyEight(myList):
    anagramPairs = []
    maxLength = 4
    for a in myList:
        for b in myList:
            if(a!=b and len(a)==len(b) and 6>len(a)>=maxLength and isAnagram(a, b)):
                if(len(a)>maxLength):
                    maxLength = len(a)
                    anagramPairs = [sorted([a,b])]
                else:
                    v = sorted([a,b])
                    if v not in anagramPairs:
                        anagramPairs.append(v)
    digitChoices = subset([0,1,2,3,4,5,6,7,8,9],maxLength)
    realDigitChoices = []
    for x in digitChoices:
        t = 0
        for y in x:
            t+=y
        if(t%9==0 or t%9==1 or t%9==4 or t%9==7):
            realDigitChoices.append(x)
    
    orderList = []
    for c in range(maxLength):
        orderList.append(c)
    orders = permutations(orderList)
    maxSquare = -1
    for myPair in anagramPairs:
        for a in realDigitChoices:
            for x in orders:
                s = ""
                for c in range(maxLength):
                    s+=str(a[x[c]])
                if s[0]!="0" and isSquare(int(s)):
                    t = getOtherNumber(myPair, s)
                    if t!=False:
                        for x in t:
                            if x[0]!="0" and isSquare(int(x)):
                                if max(int(s),int(x)) > maxSquare:
                                    maxSquare = max(int(s),int(x))
    
    return maxSquare

# Accidentally found largest prime number at first. Oops!

start = time.time()
print projectEulerProblemNinetyEight(goodContents)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

18769
--- 0.592419862747 seconds ---

for input of given list of words.
'''