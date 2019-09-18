'''
Author: Walker Kroubalkian
Exponentiation by Squaring Approach to Project Euler Problem #48
'''

import time

def lastDigitsPower(a,b,n):
    myMod = 10**n
    total = a
    powers = [a]
    e = 1
    while(e<b):
        total*=total
        total%=myMod
        powers.append(total)
        e*=2
    myBinary = (bin(b)[2:])[::-1]
    final = 1
    for c in range(len(myBinary)):
        if(int(myBinary[c])):
            final*=powers[c]
            final%=myMod
    return final

def projectEulerProblemFortyEight(i,n):
    total = 0
    myMod = 10**n
    for c in range(1,i+1):
        total+=lastDigitsPower(c, c, n)
        total%=myMod
    return total

start = time.time()
print projectEulerProblemFortyEight(1000, 10)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

9110846700
--- 0.00864911079407 seconds ---

for input of i = 1000, n = 10
'''
    