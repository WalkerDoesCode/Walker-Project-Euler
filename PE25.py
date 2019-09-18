'''
Author: Walker Kroubalkian
Logarithmic Approach to Project Euler Problem #25
'''

import time
import math

def projectEulerProblemTwentyFive(n):
    golden = (1+math.sqrt(5))/2
    return int(math.ceil(math.log(math.sqrt(5),golden)+(n-1)*math.log(10, golden)))

start = time.time()
print projectEulerProblemTwentyFive(1000)
print ("--- %s seconds ---" % (time.time() - start))

'''
Prints

4782
--- 2.121925354e-05 seconds ---

for input of n = 1000
'''