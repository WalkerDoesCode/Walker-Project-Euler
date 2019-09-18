'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #33
'''

import time

def gcd(a,b):
    if(b>a):
        return gcd(b,a)
    while(min(a,b)>0):
        temp = a%b
        a = b
        b = temp
    return max(a,b)

def projectEulerProblemThirtyThree(n):
    fractions = []
    for a in range(10,n+1):
        for b in range(10,n+1):
            c = a/10
            d = a%10
            e = b/10
            f = b%10
            if(d == e and a!=b):
                if(f*a==c*b):
                    fractions.append([a,b])
    numerator = 1
    denominator = 1
    for x in fractions:
        numerator*=x[0]
        denominator*=x[1]
    return denominator/(gcd(numerator,denominator))

start = time.time()
print projectEulerProblemThirtyThree(99)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

100
--- 0.00145101547241 seconds ---

for input of n = 99
'''