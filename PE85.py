'''
Author: Walker Kroubalkian
Combinatorial Approach to Project Euler Problem #85
'''

import time

def projectEulerProblemEightyFive(n):
    triangles = []
    c = 1
    v = 1
    while(v<=n):
        triangles.append(v)
        c+=1
        v+=c
    l = len(triangles)
    
    closestFound = -1
    smallestDiff = n
    for a in range(l):
        for b in range(a,l):
            c = triangles[a]
            d = triangles[b]
            v = abs(c*d-n)
            if(v<smallestDiff):
                smallestDiff = v
                closestFound = (a+1)*(b+1)
    return closestFound

start = time.time()
print projectEulerProblemEightyFive(2000000)
print ("--- %s seconds ---" % (time.time()-start))

'''
Prints

2772
--- 0.207247018814 seconds ---

for input of n = 2000000.
'''