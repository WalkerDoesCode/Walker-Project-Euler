'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #95
'''

import time

def projectEulerProblemNinetyFive(n):
    properSums = [0]*(n+1)
    for c in range(1,n/2+1):
        for d in range(2*c,n+1,c):
            properSums[d]+=c
    maxLoop = 5
    minNumber = 12496
    loopLengths = [-1]*(n+1)
    for e in range(n,0,-1):
        if loopLengths[e]==-1:
            t = 0
            f = properSums[e]
            loops = True
            found = [e]
            if(f!=e):
                while(f!=e):
                    t+=1
                    if(f>n):
                        for x in found:
                            loopLengths[x] = 0
                        loops = False
                        break
                    if loopLengths[f]!=-1:
                        for x in found:
                            loopLengths[x] = loopLengths[f]
                            loops = False
                            break
                    if f in found:
                        a = found.index(f)
                        for x in found:
                            loopLengths[x] = len(found)-a
                        found = found[a:]
                        break
                    found.append(f)
                    v = properSums[f]
                    if(v==f or v==0):
                        for x in found:
                            loopLengths[x] = 0
                        loops = False
                        break
                    f = v
                if loops:
                    for x in found:
                        loopLengths[x] = t
                    if t>maxLoop:
                        maxLoop = t
                        minNumber = found[0]
                        for x in found:
                            if x<minNumber:
                                minNumber = x
                    elif t==maxLoop:
                        for x in found:
                            if x<minNumber:
                                minNumber = x
                else:
                    for x in found:
                        loopLengths[x] = 0
    return minNumber
            

start = time.time()
print projectEulerProblemNinetyFive(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

14316
--- 5.02517795563 seconds ---

for input of n = 1000000.
'''