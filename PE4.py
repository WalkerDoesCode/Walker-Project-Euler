'''
Author: Walker Kroubalkian
"Bounding" Approach to Project Euler Problem #4
'''

import time

def isPalindrome(n):
    return str(n)==str(n)[::-1]

def projectEulerProblemFour(n):
    upper = 10**n - 1
    lower = 10**(n-1)
    maxFound = 0
    while(upper>=lower):
        c = upper
        while(c>=lower):
            if(isPalindrome(upper*c)):
                lower = c
                if(upper*c>maxFound):
                    maxFound = upper*c
                break
            c-=1
        upper-=1
    return maxFound

start = time.time()
print projectEulerProblemFour(3)
print("--- %s seconds ---" % (time.time() - start))

'''
Prints

906609
--- 0.00363111495972 seconds ---

for input of n = 3
'''