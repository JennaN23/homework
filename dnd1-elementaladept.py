import random

# dnd1-elementaladept.py

# You are a mage with the Fire Bolt spell. This does 1d10 damage, or 5.5
# points of damage on average. If you have the Elemental Adept feat, damage
# rolls of 1 become 2. How much more damage do you do on average if you are
# an Elemental Adept? Simulate by rolling dice a million times.

n = 1000000
sum = 0.0
nsum = 0.0

for i in range(n):
	r = random.randint(1, 10)
	if r == 1: nsum += 1
	sum  += r
	nsum += r
print((nsum/n) - (sum/n))


"""
python3 dnd1-elementaladept.py
0.1
"""
