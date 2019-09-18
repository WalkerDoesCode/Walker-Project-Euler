'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #91
'''

import time

def projectEulerProblemNinetyOne(n):
    total = 3*n*n
    squares = []
    for h in range(n+1):
        squares.append(h*h)
    for c in range(1,n+1):
        for l in range(1,(c+1)/2):
            if l*(c-l) in squares:
                total+=4
        if(c%2==0):
            total+=2
    for a in range(1,n+1):
        firstTerm = 0
        for c in range(a+1,n+1):
            firstTerm += a
            for b in range(1,n+1):
                secondTerm = squares[b]
                if((secondTerm-firstTerm)%b==0):
                    d = (secondTerm-firstTerm)/b
                    if 1<=d<=n:
                        total+=2
    return total

start = time.time()
print projectEulerProblemNinetyOne(50)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

14234
--- 0.00694298744202 seconds ---

for input of n = 50.
'''