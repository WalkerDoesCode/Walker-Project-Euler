'''
Author: Walker Kroubalkian
Recursive Approach to Project Euler Problem #31
'''

import time

def projectEulerProblemThirtyOne(n, currencies):
    currencies = sorted(currencies)[::-1]
    if(len(currencies)==1):
        if(n%currencies[0]==0):
            return 1
        else:
            return 0
    total = 0
    current = currencies[0]
    rest = currencies[1:]
    i = 0
    while(i*current<=n):
        total+=projectEulerProblemThirtyOne(n-i*current, rest)
        i+=1
    return total

start = time.time()
print projectEulerProblemThirtyOne(200, [1,2,5,10,20,50,100,200])
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

73682
--- 0.0563788414001 seconds ---

for input of n=200, currencies = [1,2,5,10,20,50,100,200]
'''