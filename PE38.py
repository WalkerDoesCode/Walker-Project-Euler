'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #38
'''

import time
from collections import Counter

def pandigital(n):
    a = str(n)
    c = 2
    while(len(a)<9):
        a+=str(n*c)
        c+=1
    if(len(a)!=9):
        return -1
    if Counter(a) == Counter("123456789"):
        return int(a)
    return -1

def projectEulerProblemThirtyEight(maxKnown):
    c = 2
    temp = maxKnown
    while(c<=4):
        start = int(str(maxKnown)[0:c]) + 1
        while(start<10**c):
            v = pandigital(start)
            if(v>temp):
                temp = v
            start+=1
        c+=1
    return temp

start = time.time()
print projectEulerProblemThirtyEight(918273645)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

932718654
--- 0.00893306732178 seconds ---

for input of n = 918273645
'''