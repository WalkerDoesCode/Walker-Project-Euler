'''
Author: Walker Kroubalkian
Order of 10 Approach to Project Euler Problem #26
'''

import time

def projectEulerProblemTwentySix(n):
    maxIndex = 1
    maxCycle = 0
    for i in range(2,n):
        temp = i
        while(temp%2==0):
            temp/=2
        while(temp%5==0):
            temp/=5
        if(temp!=1):
            e = 1
            p = 10
            while(p%temp!=1):
                p*=10
                p%=temp
                e+=1
            if(e>maxCycle):
                maxIndex = i
                maxCycle = e
    return maxIndex

start = time.time()
print projectEulerProblemTwentySix(1000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

983
--- 0.0106329917908 seconds ---

for input of n=1000
'''
