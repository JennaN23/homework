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

# w/o list
# generate random bd
# ask about formula vs simulation

ds  = int(sys.argv[1])
n   = int(sys.argv[2])
tot = 0
sim = 10

for i in range(sim):
	p   = 1
	bds = [random.randint(1, ds) for i in range(n)]
	for j in range(n):
		if bds.count([bds[j]]) > 1: break
		p *= (ds - j)/ds    # count how many birthdays per day out of total
	tot += (1 - p)
	#print(bds)
print(f'{tot/sim:.3f}')

# total #/# occurrences   100/4

"""
#variation w/o list

for i in range(sim):
	p = 1
	dup = False
	for i in range(n):
		bd = random.randint(1, ds)
		for j in range(ds):
			if j == bd: dup = True
		if dup: break 
		else: p *= (ds - j)/ds
	tot += (1 - p)
print(f'{tot/sim:.3f}')
"""

"""
python3 33birthday.py 365 23
0.571
"""
