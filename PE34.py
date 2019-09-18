'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #34
'''

import time

def factorial(n):
    total = 1
    for c in range(2,n+1):
        total*=c
    return total

def projectEulerProblemThirtyFour(n):
    factorials = []
    for x in range(10):
        factorials.append(factorial(x))
    a = 1
    while((10**a) - 1 < factorials[n]*a):
        a+=1
    
    total = 0
    final = factorials[n]*a
    for c in range(3,final+1):
        myString = str(c)
        subTotal = 0
        for x in myString:
            subTotal+=factorials[int(x)]
        if(subTotal==c):
            total+=c
    return total

start = time.time()
print projectEulerProblemThirtyFour(9)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

40730
--- 6.35254812241 seconds ---

for input of n = 9
'''