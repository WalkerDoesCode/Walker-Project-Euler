'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #36
'''

import time

def isPalindrome(x):
    return x%10!=0 and str(x) == str(x)[::-1]

def projectEulerProblemThirtySix(n):
    total = 0
    for i in range(1,n):
        if(isPalindrome(i) and isPalindrome(int(bin(i)[2:]))):
            total+=i
    return total

start = time.time()
print projectEulerProblemThirtySix(1000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

872187
--- 0.415219783783 seconds ---

for input of n = 1000000
'''