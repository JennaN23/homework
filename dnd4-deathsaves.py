import random

# dnd4-deathsaves.py

# Death saves are a little different than normal saving throws. If your
# health drops to 0 or below, you are unconscious and may die. Each time it
# is your turn, roll a d20 to determine if you get closer to life or fall
# deeper into death. If the number is less than 10, you record a "failure".
# If the number is 10 or greater, you record a "success". If you collect 3
# failures, you "die". If you collect 3 successes, you are "stable" but
# unconscious. If you are unlucky and roll a 1, it counts as 2 failures.
# If you're lucky and roll a 20, you gain 1 health and have "revived".
# Write a program that simulates death saves. What is the probability one
# dies, stabilizes, or revives?

n  = 1000
d  = 0
st = 0
r  = 0
stop = False

for i in range(n):
	f  = 0
	s  = 0
	while stop == False:
		r = random.randint(1, 20)
		if f == 3:
			d += 1
			break
		if s == 3:
			st += 1
			break
		if r == 20:
			r += 1
			break
		elif r == 1: f += 2
		elif r < 10: f += 1
		else: s += 1
print(f'die: {d/n}')
print(f'stabilize: {st/n}')
print(f'revive: {r/n}')
	
	

"""
python3 dnd4-deathsaves.py
die: 0.405
stabilize: 0.414
revive: 0.181
"""
