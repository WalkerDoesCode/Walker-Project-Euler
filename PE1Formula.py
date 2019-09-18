'''
Author: Walker Kroubalkian
The Formulaic Approach to Project Euler Problem #1
'''

from math import floor
import time

def projectEulerProblemOne(n):
    numberThrees = floor((n-1)/3)
    numberFives = floor((n-1)/5)
    numberFifteens = floor((n-1)/15)
    
    addThrees = 3*numberThrees*(numberThrees+1)/2
    addFives = 5*numberFives*(numberFives+1)/2
    addFifteens = 15*numberFifteens*(numberFifteens+1)/2
    
    return int(addThrees + addFives - addFifteens)

start = time.time()
print projectEulerProblemOne(1000)
print("--- %s seconds ---" % (time.time() - start))

'''
Prints

233168
--- 2.19345092773e-05 seconds ---

for input of n = 1000
'''