import argparse
import gzip
import mcb185

# 62orfs.py

# Make a program that finds open reading frames in the E. coli genome
# Your program should read a fasta file
# There should be an optional minimum ORF size with a default value of 300 nt
# The output should be a table showing 4 columns
#     1. parent sequence identifier
#     2. begin coordinate
#     3. end coordinate
#     4. strand
#     5. first 10 amino acids of the protein

# Hint: use argparse, mcb185.read_fasta(), and mcb185.translate()
# Hint: don't use the whole genome for testing

# Note: your genes should be similar to those in the real genome

# 5' - ATG AAA TAA TAG- 3'
# 3' - TAC TTT ATT ATC- 5' complement
# 5' - CTA TTA TTT CAT - 3' reverse complement 

def find_end(seq, start):
	for i in range(start, len(seq) - 2, 3):
		cod = seq[i:i + 3]
		if cod == 'TAA' or cod == 'TGA' or cod == 'TAG':
			if (i + 3) - start > min and (i + 3) not in orfs:
				return i + 3
			else: break
		
def find_starts(seq, frame, is_rc):
	for i in range(frame, len(seq) - 2, 3):
		cod = seq[i:i + 3]
		if cod == 'ATG':
			start = i
			stop = find_end(seq, start)
			if stop == None: continue
			if is_rc:
				orfs[len(seq) - start] = [len(seq) - stop + 1]
			else:
				orfs[stop] = [start + 1]
			
def find_orfs(seq, min, is_rc, id):
	anti = mcb185.rc(seq)
	for frame in range(3):
		find_starts(seq, frame, is_rc)
		for orf in orfs:
			if is_rc:
				orfs[orf].append(mcb185.translate(seq[len(seq) - orf:]))
				orfs[orf].append(f'-')
			else:
				orfs[orf].append(mcb185.translate(seq[orfs[orf][0] - 1:]))
				orfs[orf].append(f'+')
			orfs[orf].append(id)
# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<file>', help='some file')

# optional arguments with default parameters
parser.add_argument('-min', required=False, type=int, default=300,
	metavar='<int>', help='minimum ORF size [%(default)s]')

# finalization
arg = parser.parse_args()


filename = arg.file
min      = arg.min
orfs     = {}

for name, seq in mcb185.read_fasta(filename):
	f = name.split()
	id = f[0]
	anti = mcb185.rc(seq)
	find_orfs(seq, min, False, id)
	find_orfs(anti, min, True, id)
	
for key, val in sorted(orfs.items(), key=lambda item: item[1]):
	start  = val[0]
	stop   = key
	strand = val[2]
	aas    = val[1][:10] 
	id     = val[3] 
	print(f'{id} {start} {stop} {strand} {aas}')
	
		
# find start, stop, then translate
# find orf, then skip
# use dictionary of end coordinates as key?	
# reverse complement
# iterate through frame (0, 1, 2)  (3 for loops (nested))
# go through whole sequence, find orf (set val to true)
# store end as key, check to see if key already in dict
# store print as tuple as value, sort using start coordinate
# sorted(dictionary.values())
	

"""
python3 62orfs.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz
NC_000913.3 108 500 - MVFSIIATRW
NC_000913.3 337 2799 + MRVLKFGGTS
NC_000913.3 2801 3733 + MVKVYAPASS
NC_000913.3 3512 4162 - MSHCRSGITG
NC_000913.3 3734 5020 + MKLYNLKDHN
NC_000913.3 3811 4119 - MVTGLSPAIW
NC_000913.3 5310 5738 - MKIPPAMANW
NC_000913.3 5683 6459 - MLILISPAKT
NC_000913.3 6529 7959 - MPDFFSFINS
NC_000913.3 7366 7773 + MKTASDCQQS
"""
