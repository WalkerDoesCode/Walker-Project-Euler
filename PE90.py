'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #90
'''

import time

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

def projectEulerProblemNinety():
    total = subset(["0","1","2","3","4","5","6","7","8","9"],6)
    simpleSquares = ["01","04","25","81"]
    complexSquares = ["09","16","36","49","64"]
    allFound = []
    for a in total:
        for b in total:
            if(a!=b):
                possible = True
                for x in simpleSquares:
                    if not ((x[0] in a and x[1] in b) or (x[1] in a and x[0] in b)):
                        possible = False
                        break
                for y in complexSquares:
                    for c in y:
                        if c!="6" and c!="9":
                            letter = c
                            break
                    if not ((letter in a and ("6" in b or "9" in b)) or (letter in b and ("6" in a or "9" in a))):
                        possible = False
                        break
                
                if possible:
                    myPair = sorted([a,b])
                    if myPair not in allFound:
                        allFound.append(myPair)
    return len(allFound)

start = time.time()
print projectEulerProblemNinety()
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1217
--- 0.110777139664 seconds ---

for given problem.
'''