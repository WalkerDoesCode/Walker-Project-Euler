'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #74
'''

import time

def digitFactorial(n):
    factorials = [1,1,2,6,24,120,720,5040,40320,362880]
    total = 0
    for x in str(n):
        total+=factorials[int(x)]
    return total

def projectEulerProblemSeventyFour(n,v):
    loops = [-1]*(n)
    loops[0] = 0
    loops[1] = 1
    for x in range(2,n):
        if(loops[x]==-1):
            temp = x
            found = []
            alreadyDone = False
            loopLength = -1
            while(temp not in found):
                if(temp<n and loops[temp]!=-1):
                    loopLength = loops[temp]
                    alreadyDone = True
                    loops[x] = len(found)+loopLength
                    break
                found.append(temp)
                temp = digitFactorial(temp)
            if not alreadyDone:
                myIndex = found.index(temp)
                loopLength = len(found)-myIndex
                for a in range(myIndex,len(found)):
                    loops[found[a]] = loopLength
                loops[x] = len(found)
    total = 0
    for a in loops:
        if a == v:
            total+=1
    return total

start = time.time()
print projectEulerProblemSeventyFour(1000000, 60)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

402
--- 3.78305602074 seconds ---

for input of n = 1000000, v = 60.
'''