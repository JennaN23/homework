import random

# dnd3-savingthrow.py

# One of the core mechanics of D&D is the "saving throw". When certain
# events happen, you need to roll a d20 to figure out if you succeed or not.
# For example, you are walking across a frozen lake and it begins to crack
# underfoot. If you make a saving throw, you step aside. If you fail, you
# fall in. Some saving throws are more difficult than others. If the ice
# is very thick, the "difficulty class" (DC) may be only 5. This means you
# only need to roll a 5 or higher to succeed. However, if the ice is thin
# and has a DC of 15, you will need a roll of 15 or higher to succeed.
# Certain events may give you "advantage" or "disadvantage". For example,
# if you have a rope tied around your waist and a friend is instructed to
# pull you aside if anything bad happens, you could have "advantage". This
# allows you to roll two d20s and take the larger value. You may also have
# disadvantage, for example another "friend" pushes you from behind, causing
# you to stumble forward. In this case, you have "disadvantage" and must take
# the lower of two d20 rolls.

# Write a program that simulates saving throws against DCs of 5, 10, and 15.
# What is the probability of success normally or with advantage/disadvantage?
# Make a table showing the results.

n = 1000
s = 0
a = 0
d = 0

for i in range(5, 16, 5):
	s = 0
	a = 0
	d = 0
	for j in range(n):
		r = random.randint(1, 20)
		r2 = random.randint(1, 20)
		if r2 > r: 
			ra = r2
			rd = r
		else:
			rd = r2
			ra = r
		if r  >= i: s += 1	  #normal
		if ra >= i: a += 1	  #advantage
		if rd >= i: d += 1	  #disadvantage
	print(f'{i} {s/n:.3f} {a/n:.3f} {d/n:.3f}')
	
	

"""
python3 dnd3-savingthrow.py
5  0.800 0.960 0.640
10 0.550 0.797 0.302
15 0.300 0.510 0.090
"""
