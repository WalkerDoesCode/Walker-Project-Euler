'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #44
'''

import time

def projectEulerProblemFortyFour(n):
    myPentagons = [1,5]
    c = 3
    minDifference = 10**30
    while(c<=n):
        myPentagons.append(c*(3*c-1)/2)
        c+=1
    for a in myPentagons:
        for b in myPentagons:
            if(2*b<=a):
                if (a-b) in myPentagons:
                    if (a-2*b) in myPentagons:
                        if (a-2*b) < minDifference:
                            minDifference = (a-2*b)
            else:
                break
    return minDifference

start = time.time()
print projectEulerProblemFortyFour(4000)
print ("--- %s seconds ---" % (time.time()-start))


'''
Prints

5482660
--- 227.999250889 seconds ---

for input of n = 4000
'''