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

seq = ''
coords = {}
aas = []
scs = {}

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		f = line.split()
		pat1 = '\W+CDS\W+(\d+)..(\d+)'
		pat2 = '\W+CDS\W+complement\((\d+)..(\d+)'
		pat3 = '\W+\/translation=.(\w+)'
		match = re.search(pat1, line)
		if match: 
			#print(match.group(1), match.group(2))
			coords[match.group(1), match.group(2)] = '+'
		match2 = re.search(pat2, line)
		if match2:
			#print(match2.group(1), match2.group(2))
			coords[match2.group(1), match2.group(2)] = '-'
		match3 = re.search(pat3, line)
		if match3:
			#print(match3.group(1))
			aas.append(match3.group(1))
		if f[0].isdigit() == False: continue
		seq += f[1] + f[2] + f[3] + f[4] + f[5] + f[6]

length = len(seq)	
seq    = seq.upper()	
rseq   = mcb185.rc(seq)

for key, val in coords.items():
    # index starts at 0 for comp sci, 1 for bio
	#print(start, end, val)
	if val == '+':
		start = int(key[0]) - 1
		end = int(key[1])
		cds = seq[start:end]
		#print(cds)
		#print(mcb185.translate(cds))
		sc = cds[0:3]
		#print(sc)
	else: 
		start = int(key[0])
		end = int(key[1])
		cds = rseq[length - end:length - start]
		#print(cds)
		sc = cds[0:3]
		#print(sc)
	if sc not in scs: scs[sc] = 0
	scs[sc] += 1
	#print(scs)

aas = []

for sc, count in sorted(scs.items(), key=lambda item: item[1]):
	aas.append((sc, count))
	print(f'{sc} {count}')

"""
for i in range(len(aas) - 1, -1, -1):
	print(f'{aas[i][0]} {aas[i][1]}')		
"""

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
