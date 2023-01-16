import random

# 25atseq.py

# Write a program that stores random DNA sequence in a string
# The sequence should be 30 nt long
# On average, the sequence should be 60% AT
# Calculate the actual AT fraction while generating the sequence
# Report the length, AT fraction, and sequence

# Note: set random.seed() if you want repeatable random numbers

dna = ""
at = 0
seed = random.seed(1)

for i in range(30):
	r = random.choice('AAACCGGTTT')
	if r == 'A' or r == 'T': at += 1
	dna += r
print(len(dna), at/len(dna), dna)


"""
python3 25atseq.py
30 0.6666666666666666 ATTACCGTAATCTACTATTAAGTCACAACC
"""
