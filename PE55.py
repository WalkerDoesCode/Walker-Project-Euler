'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #55
'''

import time

def isPalindrome(x):
    a = str(x)
    return a == a[::-1]

def projectEulerProblemFiftyFive(n,m):
    final = 0
    for x in range(1,n+1):
        total = x
        found = False
        for a in range(m):
            total = total+int(str(total)[::-1])
            if(isPalindrome(total)):
                found = True
                break
        if not found:
            final+=1
    return final

start = time.time()
print projectEulerProblemFiftyFive(10000, 50)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

249
--- 0.0513601303101 seconds ---

for input of n = 10000, m = 50
'''