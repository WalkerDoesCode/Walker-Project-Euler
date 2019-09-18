'''
Author: Walker Kroubalkian
Sieve Approach to Project Euler Problem #23
'''

import time

def projectEulerProblemTwentyThree(n):
    sums = [0]*(n+1)
    for i in range(2, n/2+1):
        for c in range(2*i, n+1, i):
            sums[c]+=i
    
    abundant = []
    for i in range(n+1):
        if(sums[i]>i):
            abundant.append(i)
    
    possible = [True]*(n+1)
    possible[0] = False
    
    for a in abundant:
        for b in abundant:
            if(b>a or (a+b)>n):
                break
            possible[a+b] = False
    
    total = 0
    for i in range(n+1):
        if(possible[i]):
            total += (i)
    
    return total

start = time.time()
print projectEulerProblemTwentyThree(28123)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

4179871
--- 0.863159894943 seconds ---

for input of n=28123
'''