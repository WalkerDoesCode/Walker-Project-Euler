'''
Author: Walker Kroubalkian
Dynamic Approach to Project Euler Problem #92
'''

import time

def squareDigits(x):
    a = str(x)
    total = 0
    for b in a:
        total+=int(b)**2
    return total

def projectEulerProblemNinetyTwo(n):
    found = [-1]*(n)
    found[1] = 1
    found[89] = 89
    total = 0
    for c in range(n-1,1,-1):
        endsOne = True
        if(found[c]==-1):
            temp = c
            change = []
            while(temp!=89 and temp!=1 and (temp>n or found[temp]==-1)):
                if(temp<=c):
                    change.append(temp)
                temp = squareDigits(temp)
            if(temp == 89 or found[temp] == 89):
                endsOne = False
                total+=1
            if endsOne:
                for x in change:
                    found[c] = 1
            else:
                for x in change:
                    found[c] = 89
        else:
            if(found[c] == 89):
                total+=1
    return total

start = time.time()
print projectEulerProblemNinetyTwo(10000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

8581146
--- 105.508774042 seconds ---

for input of n = 10000000.
'''