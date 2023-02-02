# 27frame.py

# Write a program that prints out the position, frame, and letter of the DNA


# Note: use 0-based indexing for position and frame (biology uses 1-based)

dna = 'ATGGCCTTT'

for i in range(len(dna)):
	print(f'{i} {i % 3} {dna[i]}')

"""	
# Variation: try coding this with a single loop and nested loops

for i in range(len(dna)):
	for j in range(3):
		if   j == 0: print(i,end=' ')
		elif j == 1: print(i % 3,end=' ')
		else:        print(dna[i])
"""

"""
python3 27frame.py
0 0 A
1 1 T
2 2 G
3 0 G
4 1 C
5 2 C
6 0 T
7 1 T
8 2 T
"""
