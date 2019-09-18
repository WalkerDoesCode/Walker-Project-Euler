'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #20
'''

import time

def projectEulerProblemTwenty(n):
    total = 1
    for i in range(2,n+1):
        if(total%10==0):
            total/=10
        total*=i
    a = str(total)
    final = 0
    for l in a:
        final+=int(l)
    return final

start = time.time()
print projectEulerProblemTwenty(100)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

648
--- 0.000115871429443 seconds ---

for input of n=100
'''