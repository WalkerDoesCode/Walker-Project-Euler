'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #65
'''

import time

def gcd(a,b):
    if(min(a,b)<0):
        return gcd(abs(a),abs(b))
    if(min(a,b)==0):
        return max(a,b)
    if(a>b):
        return gcd(b,a%b)
    return gcd(a,b%a)

def projectEulerProblemSixtyFive(n):
    denominatorList = [1,0]
    for c in range(n):
        if(c%3==2):
            denominatorList.append((c+1)*2/3)
        else:
            denominatorList.append(1)
    curNumerator = 1
    curDenominator = 0
    order = denominatorList[::-1]
    for x in order:
        n = curDenominator+curNumerator*x
        d = curNumerator
        g = gcd(n,d)
        if(g==0):
            g = 1
        curNumerator = n/g
        curDenominator = d/g
    total = 0
    for x in str(curNumerator):
        total+=int(x)
    return total

start = time.time()
print projectEulerProblemSixtyFive(100)
print ("--- %s seconds ---" % (time.time() - start))

'''
Prints

272
--- 0.00275802612305 seconds ---

for input of n = 100.
'''