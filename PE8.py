'''
Author: Walker Kroubalkian
Brute Force Approach to Project Euler Problem #8
'''

import time

f = open("PE8Grid.txt","r")

if f.mode == "r":
    contents = f.readlines()
    realContents = []
    for x in contents:
        if(x[len(x)-1] == "\n"):
            realContents.append(x[0:len(x)-1])
        else:
            realContents.append(x)
else:
    raise ValueError("Cannot read from file")

def projectEulerProblemEight(lines, n):
    s = ""
    maxProduct = 0
    for x in lines:
        s+=x
    length = len(s)
    for i in range(length-n):
        total = 1
        for j in range(n):
            total*=int(s[i+j])
        if(total>maxProduct):
            maxProduct = total
    return maxProduct

start = time.time()
print projectEulerProblemEight(realContents, 13)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

23514624000
--- 0.00584602355957 seconds ---

for input of n = that crazy number
'''