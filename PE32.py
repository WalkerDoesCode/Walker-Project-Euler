'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #32
'''

import time

def listPermutations(myList):
    if(len(myList)==1):
        return [myList]
    a = myList[0]
    b = listPermutations(myList[1:])
    total = []
    for x in b:
        for c in range(len(x)+1):
            temp = x[0:c]
            temp.append(a)
            temp.extend(x[c:])
            total.append(temp)
    return total

def projectEulerProblemThirtyTwo(myList):
    myList = listPermutations(myList)
    total = []
    for a in myList:
        b = 10*a[0]+a[1]
        c = 100*a[2]+10*a[3]+a[4]
        d = 1000*a[5]+100*a[6]+10*a[7]+a[8]
        if(b*c==d):
            if d not in total:
                total.append(d)
        b = a[0]
        c = 1000*a[1]+100*a[2]+10*a[3]+a[4]
        d = 1000*a[5]+100*a[6]+10*a[7]+a[8]
        if(b*c==d):
            if d not in total:
                total.append(d)
    final = 0
    for x in total:
        final+=x
    return final

start = time.time()
print projectEulerProblemThirtyTwo([1,2,3,4,5,6,7,8,9])
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

45228
--- 0.590600013733 seconds ---

for input of [1,2,3,4,5,6,7,8,9]
'''