'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #22
'''

import time

f = open("PE22Names.txt","r")

if(f.mode == "r"):
    contents = f.readlines()
    realContents = []
    for x in contents:
        realContents.append(x.split(","))
else:
    raise ValueError("Cannot read from file")

finalList = realContents[0]

def getValueString(myString):
    total = 0
    
    for x in myString:
        if("A"<=x<="Z"):
            total+=(ord(x)-ord("A")+1)

    return total

def projectEulerProblemTwentyTwo(nameList):
    nameList = sorted(nameList)
    total = 0
    numberNames = len(nameList)
    for i in range(numberNames):
        total+=(i+1)*getValueString(nameList[i])
    return total

start = time.time()
print projectEulerProblemTwentyTwo(finalList)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

871198282
--- 0.00785303115845 seconds ---

for input of given list of names
'''