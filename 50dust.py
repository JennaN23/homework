#!/usr/bin/env python3

import argparse
import math
import mcb185
import subprocess
import sys

# 50dust.py

# Write a better version of your 42dust.py program
# Your program must have the following properties

# 1. has option and default value for window size
# 2. has option and default value for entropy threshold
# 3. has a switch for N-based or lowercase (soft) masking
# 4. works with uppercase or lowercase input files
# 5. works as an executable
# 6. outputs a FASTA file wrapped at 60 characters

# Optional: make the algorithm faster (see 29gcwin.py for inspiration)
# Optional: benchmark your programs with different window sizes using time

# Hint: make a smaller file for testing (e.g. e.coli.fna in the CLI below)

def acgt_prob(seq):
	a    = 0
	c    = 0
	g    = 0
	t    = 0
	tot  = 0
	for nt in seq:
		if   nt == 'A': a += 1
		elif nt == 'C': c += 1
		elif nt == 'G': g += 1
		else:           t += 1
		tot += 1
	probs = [a/tot, c/tot, g/tot, t/tot]
	return probs
		
def entropy(probs):
	h = 0
	for val in probs:
		if val == 0: continue
		h += val*math.log2(val)
	return -h
	
def wrap(seq, wl):
	for i in range(0, len(seq), wl):
		yield seq[i:i + wl]

# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<file>', help='some file')

# optional arguments with default parameters
parser.add_argument('-w', required=False, type=int, default=11,
	metavar='<int>', help='window size [%(default)s]')
parser.add_argument('-t', required=False, type=float, default=1.4,
	metavar='<int>', help='entropy threshold [%(default)i]')

# switches
parser.add_argument('-s', action='store_true',
	help='on/off switch')

# finalization
arg = parser.parse_args()

"""
# testing
print(arg.file)
print(arg.w, arg.t)
if arg.s: print('switch on')
else:     print('switch off')
"""

info = ''
seqs = []

for name, seq in mcb185.read_fasta(arg.file):
		seq = seq.upper()
		# calculate ACGT probs
		for nt in seq:
			seqs.append(nt)

for name, seq in mcb185.read_fasta(arg.file):
	seq = seq.upper()
	for i in range(len(seq) - arg.w + 1):
		w  = seq[i:i + arg.w]
		probs = acgt_prob(w)
		assert(math.isclose(sum(probs), 1.0))
		h = entropy(probs)
		if h < arg.t: 
			if arg.s: seqs[i:i + arg.w] = w.lower()
			else: seqs[i: i + arg.w] = 'N' * arg.w
	print(f'>{name}')
	seq =''.join(seqs)
	for line in wrap(seq, 60): print(line)

	
"""
python3 50dust.py -w 11 -t 1.4 -s e.coli.fna  | head
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGcttttcattctGACTGCAACGGGCAATATGTCTCTGTGTggattaaaaaaagagtgTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGagtaaattaaaattttattgaCTTAGG
TCACtaaatactttaaCCAATATAGGCATAGCGCACAGacagataaaaattacaGAGTac
acaacatccaTGAAACGCATTAGCACCACCATtaccaccaccatcaccaTTACCACAGGT
AACggtgcgggctgACGCGTACAGgaaacacagaaaaaagccCGCACCTGACAGTGCggg
ctttttttttcgaCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
AggcaggggcaggtggCCAccgtcctctctgcccccgccaaaatcaccaaccacctGGTG
GCGATgattgaaaaaaccattaGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
"""
