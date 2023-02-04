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


# ask about reads being full length

gs    = int(sys.argv[1])
rn    = int(sys.argv[2])
rl    = int(sys.argv[3])
reads = []
cvg   = []

for i in sys.argv[1:]:
	try:
		p = int(i)
	except:
		raise ValueError(f'Cannot convert {i} to number')
		
#generate starting coordinate, if start + rl < gs, add tuple

for i in range(rn):
	s = random.randint(-rl + 1, gs + rl)
	#s = random.randint(1, gs)
	#while (s + rl - 1) > gs: s = random.randint(1, gs) 
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
p, min = cvg[0]
p, max = cvg[0]

for p, c in cvg:
	tc += c
	if c < min: min = c
	if c > max: max = c 
ac  = tc/gs

print(f'{min} {max} {ac:.5f}')

"""
python3 32xcoverage.py 1000 100 100
5 20 10.82375
"""
