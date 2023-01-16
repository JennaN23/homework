# 26anti.py

# Write a program that prints the reverse-complement of a DNA sequence
# You must use a loop and conditional

# Variation: try this with the range() function and slice syntax

dna  = 'ACTGAAAAAAAAAAA'

for i in range(len(dna), -1, -1):
	nt = dna[i-1]
	if   nt == 'A': print('T',end='')
	elif nt == 'C': print('G',end='')
	elif nt == 'G': print('C',end='')
	else: print('A',end='')
print()
	

"""
python3 26anti.py
TTTTTTTTTTTCAGT
"""
