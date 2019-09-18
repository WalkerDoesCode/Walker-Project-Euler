'''
Author: Walker Kroubalkian
Brute Force ApproachProject Euler Problem #29
'''

import time

def projectEulerProblemTwentyNine(n):
    checked = [False]*(n+1)
    checked[0] = True
    checked[1] = True
    total = 0
    for i in range(2,n+1):
        if(not checked[i]):
            p = 0
            power = i
            while(power<=n):
                checked[power] = True
                power*=i
                p+=1
            possible = [False]*(p*n+1)
            for a in range(1,p+1):
                for b in range(2,n+1):
                    possible[a*b] = True
            for x in possible:
                if x:
                    total+=1
    return total

start = time.time()
print projectEulerProblemTwentyNine(100)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

9183
--- 0.000976085662842 seconds ---

for input of n=100
'''