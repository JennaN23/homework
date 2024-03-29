import gzip
import mcb185
import re
import sys

# 63canonical.py

# You probably learned that ATG is the only start codon, but is it?
# Write a program that reports the start codons from the E. coli genome
# Your program must:
#    1. read GCF_000005845.2_ASM584v2_genomic.gbff.gz at the only input
#    2. use a regex to find CDS coordinates
#    3. count how many different start codons there are

# Note: the sequence is at the end of the file
# Note: genes on the negative strand are marked complement(a..b)

# Hint: you can read a file twice, first to get the DNA, then the CDS
# Hint: check your CDS by examining the source protein

# did not include 'join'

seq = ''
coords = {}
aas = []
scs = {}

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		pat1 = '\s{5}CDS\s+(\d+)..(\d+)'
		pat2 = '\s{5}CDS\s+complement\((\d+)..(\d+)'
		pat3 = '\W+\/translation=.(\w+)'
		match = re.search(pat1, line)
		if match: 
			coords[match.group(1), match.group(2)] = '+'
		match2 = re.search(pat2, line)
		if match2:
			coords[match2.group(1), match2.group(2)] = '-'
		match3 = re.search(pat3, line)
		if match3:
			aas.append(match3.group(1))
		if f[0].isdigit() == False: continue
		seq += f[1] + f[2] + f[3] + f[4] + f[5] + f[6]

length = len(seq)	
seq    = seq.upper()	
rseq   = mcb185.rc(seq)

for key, val in coords.items():
	# index starts at 0 for comp sci, 1 for bio
	if val == '+':
		start = int(key[0]) - 1
		end = int(key[1])
		cds = seq[start:end]
		sc = cds[0:3]
	else: 
		start = int(key[0])
		end = int(key[1])
		cds = rseq[length - end:length - start]
		sc = cds[0:3]
	if sc not in scs: scs[sc] = 0
	scs[sc] += 1

aas = []

for sc, count in sorted(scs.items(), key=lambda item: item[1], reverse=True):
	aas.append((sc, count))
	print(f'{sc} {count}')


"""
python3 63canonical.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gbff.gz
ATG 3883
GTG 338
TTG 80
ATT 5
AGT 1
AAA 1
AGC 1
TTC 1
TAA 1
CGT 1
CTG 2
GAC 1
"""
