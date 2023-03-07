import argparse
import gzip
import mcb185
import re

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

# 5' - ATG AAA TAA - 3'
# 3' - TAC TTT ATT - 5' complement
# 5' - TTA TTT CAT - 3' reverse complement 

def find_orfs(dna, min, is_comp):
	if is_comp: 
		dna = mcb185.rc(dna)
		#print(dna[len(dna) - 500:len(dna) - 497], dna[len(dna) - 110:len(dna) - 107])
		# stop = length - 110: length - 107
		print(dna[len(dna) - 500:len(dna) - 497], dna[len(dna) - 110:len(dna) - 107])
		#print(dna[len(dna) - 4162:len(dna) - 4159], dna[len(dna) - 3514:len(dna) - 3511])
		#print(len(dna) - 500, len(dna) - 497, len(dna) - 110, len(dna) - 107)
		#print(dna[107:110], dna[497:500])
	for frame in range(3):
		current_start = frame
		#print('new frame', frame, (len(dna) - current_start - 2))
		# look for start
		while current_start < (len(dna) - current_start - 2):
			orf_found = False
			cod = dna[current_start:current_start + 3]
			#if current_start >= 100: print(current_start, cod)
			if cod == 'ATG': 
				# found start
				#print(j)
				start = current_start + 1
				current_stop = current_start
				# look for stop
				while current_stop < (len(dna) - current_start - 2) and not orf_found:
					cod2 = dna[current_stop:current_stop + 3]
					l = (current_stop + 3) - start
					#print(cod, start, cod2, l, l > arg.min)
					min_orf = l >= min
					if (cod2 =='TAA' or cod2 == 'TGA' or cod2 == 'TAG'):
						if min_orf:
							stop = current_stop + 3
							#print(cod, cod2, stop, start, l, min_orf)
							aas = mcb185.translate(dna[current_start:stop])
							if stop not in orfs: 
								# stop = length - 110: length - 107
								if is_comp:
									# key with end, strand
									#print(cod, cod2, stop, start, l, len(dna) - stop)
									orfs[len(dna) - start - 2, '-'] = (len(dna) - stop, aas[:10], frame)
								else:
									orfs[stop, '+'] = (start, aas[:10], frame)
							#print(orfs)
							orf_found = True
							current_start = current_stop
							#print(frame, current_start, current_stop, stop)
							# look for next orf
							break
						else: break   # found stop, but too short
					current_stop += 3
			current_start += 3

# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<file>', help='some file')

# optional arguments with default parameters
parser.add_argument('-min', required=False, type=int, default=300,
	metavar='<int>', help='minimum ORF size [%(default)s]')

# finalization
arg = parser.parse_args()

orfs = {}

for name, seq in mcb185.read_fasta(arg.file):
	f = name.split()
	id = f[0]

#find_orfs(seq, arg.min, False)
find_orfs(seq, arg.min, True)

for key, val in sorted(orfs.items(), key=lambda item: item[0]):
	stop = key[0]
	start = val[0]
	aas = val[1]
	strand = key[1]
	frame = val[2]
	print(f'{id} {start} {stop} {strand} {aas} {frame}')

#rdna = mcb185.rc(dna)
#print(dna[2800:2803], dna[3730:3733])
#print(dna[2800:2803], dna[3730:3733])
		
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
