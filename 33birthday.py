import math
import sys
import random

# 33birthday.py

# You may have heard of the 'birthday paradox' before
# https://en.wikipedia.org/wiki/Birthday_problem
# Write a program that simulates it
# Make the number of days and the number of people command line arguments

# Hint: make the problem smaller to aid visualization and debugging

# Variation: try making the calendar a list
# Variation: try making the birthdays a list

# generate random bd
# simulation

# initialize with zeros, mark each bd, if 0 continue, if 1 break

for val in sys.argv[1:]:
	try:
		p = int(val)
	except:
		raise ValueError(f'Cannot convert {val} to int')
	assert(p > 0)
		
ds  = int(sys.argv[1])
n   = int(sys.argv[2])
sim = 1000
tot = 0

for i in range(sim):
	bds = [0] * ds
	for j in range(n):
		bd = random.randint(0, ds - 1)
		if bds[bd] == 1:
			tot += 1 
			break
		bds[bd] += 1
print(f'{tot/sim:.3f}')


"""
# Variation

ds  = int(sys.argv[1])
n   = int(sys.argv[2])
tot = 0
sim = 1000

for i in range(sim):
	bds = [random.randint(1, ds) for i in range(n)]
	for j in range(n):
		if bds.count(bds[j]) > 1: 
			tot += 1
			break
print(f'{tot/sim:.3f}')
"""

"""
python3 33birthday.py 365 23
0.571
"""
