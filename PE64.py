'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #64
'''

import time
from math import floor
from decimal import *

getcontext().prec = 214

def gcd(a,b):
    if(a<0 or b<0):
        return gcd(abs(a),abs(b))
    if(min(a,b)==0):
        return max(a,b)
    if(a>b):
        return gcd(b,a%b)
    return gcd(a,b%a)


def projectEulerProblemSixtyFour(n):
    total = 0
    for e in range(2,n+1):
        v = Decimal(e).sqrt()
        if(int(v)*int(v)!=e):  
            fractions = []
            root = [1,1]
            constant = [0,1]
            denominators = []
            while [root,constant] not in fractions:
                fractions.append([root,constant])
                a = root[0]
                b = root[1]
                c = constant[0]
                d = constant[1]
                x = int(floor(v))
                denominators.append(x)
                v = Decimal(1.)/(Decimal(v)-Decimal(int(v)))
                
                newRootN = a*b*d*d
                newRootD = a*a*d*d*e-b*b*c*c-x*x*b*b*d*d+2*b*b*x*c*d
                newConstantN = x*b*b*d*d-b*b*c*d
                newConstantD = newRootD
                
                g1 = gcd(newRootN,newRootD)
                g2 = gcd(newConstantN,newConstantD)

                newRootN/=g1
                newRootD/=g1
                newConstantD/=g2
                newConstantN/=g2
                if(newRootD<0):
                    newRootN = -newRootN
                    newRootD = -newRootD
                if(newConstantD<0):
                    newConstantD = -newConstantD
                    newConstantN = -newConstantN
                root = [newRootN,newRootD]
                constant = [newConstantN,newConstantD]
            period = len(fractions) - fractions.index([root,constant])
            if(period%2==1):
                total+=1
            
    return total

start = time.time()
print projectEulerProblemSixtyFour(10000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

1322
--- 12.4575679302 seconds ---

for input of n = 10000.
'''