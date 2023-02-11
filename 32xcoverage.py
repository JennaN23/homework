import random
import sys

# 32xcoverage.py

# Write a program that simulates a shotgun resequencing project
# How uniformly do the reads "pile up" on a chromosome?
# How much of that depends on sequencing depth?

# Report min, max, and average coverage
# Make variables for genome size, read number, read length
# Input values from the command line

# Hint: make the problem smaller, so it's easier to visualize and debug
# Hint: if you don't understand the context of the problem, ask for help
# Hint: if you are undersampling the ends, do something about it

# Note: you will not get exactly the same results as the command line below

# ask about reads being full length (make sure reads fit within the sequence)
# for pos in range(len(grn) - readlen + 1)
# initialize with zeros

gs    = int(sys.argv[1])
rn    = int(sys.argv[2])
rl    = int(sys.argv[3])
reads = []
cvg   = []

for val in sys.argv[1:]:
	try:
		p = int(val)
	except:
		raise ValueError(f'Cannot convert {val} to number')
	assert(p > 0)
		
#generate starting coordinate, if start + rl < gs, add tuple

for i in range(rn):
	s = random.randint(1, gs - rl)
	e = s + rl - 1
	reads.append((s, e))
reads.sort()
	
# store position and coverage as tuple
# at each position, how many reads

for p in range(1, gs + 1):
	c = 0
	for s, e in reads:
		if s <= p and e >= p: c += 1
	cvg.append((p, c))
#print(cvg)

tc = 0
p, min = cvg[rl]
p, max = cvg[rl]

# don't sample the ends

for p, c in cvg:
	if p < rl//2 or p > gs - rl//2: continue
	tc += c
	if c < min: min = c
	if c > max: max = c 
ac = tc/gs

print(f'{min} {max} {ac:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
