'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #43
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

def projectEulerProblemFortyThree(myList):
    a = listPermutations(myList)
    total = 0
    for x in a:
        y = ""
        for b in x:
            y+=str(b)
        if(y[0]!="0" and int(y[7:10])%17==0 and int(y[6:9])%13==0 and int(y[5:8])%11==0 and int(y[4:7])%7==0 and int(y[3:6])%5==0 and int(y[2:5])%3==0 and int(y[1:4])%2==0):
            total+=int(y)
    return total

start = time.time()
print projectEulerProblemFortyThree([0,1,2,3,4,5,6,7,8,9])
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

16695334890
--- 10.1015229225 seconds ---

for input of myList =[0,1,2,3,4,5,6,7,8,9]
'''