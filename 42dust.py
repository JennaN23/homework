import gzip
import math
import mcb185
import sys

# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)

file = sys.argv[1]
ws   = int(sys.argv[2])
ht   = float(sys.argv[3])
info = ''
seqs = []

with gzip.open(file, 'rt') as fp:
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'): continue
		# calculate ACGT probs
		for nt in line:
			seqs.append(nt)


ind   = -1
#print(probs)
#print(seqs[:11])

with gzip.open(file, 'rt') as fp:
	for line in fp.readlines():
		line = line.rstrip()
		if line.startswith('>'): 
			print(line)
			continue
		for i in range(len(line) - ws + 1):
			w = line[i:i + ws]
			ind += 1
			#calculate entropy
			probs = mcb185.acgt_prob(w)
			assert(math.isclose(sum(probs), 1.0))
			h = mcb185.entropy(probs)
			#print(h)
			if h < ht: seqs[ind] = 'N'
#print(seqs)
seq =''.join(seqs)

for i in range(0, len(seq), 60):
	print(seq[i:i+60])
			
			

#seqs = mcb185.read_fasta(file)
#print(seqs)

"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNTTTTCATTCTGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNAAAAAGAGTGTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNATTTTATTGACTTAGG
TCACNNAATACTTTAACCAATATAGGCATAGCGCACAGNCNNNNAAAAATTACAGAGTNN
ACAACATCCATGAAACGCATTAGCACCACCATNNNNNNNACCATCACCATTACCACAGGT
AACNGTGCGGGCTGACGCGTACAGNNNNNNNNGAAAAAAGCCCGCACCTGACAGTGCNNN
NNNTTTTTTTCGACCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNCANGGGCAGGTGGCCANCGNNNNNNNTNNNCCCGNNNNNNNNNCCAACCACCTGGTG
GCGATNATTGNNAAAACCATTAGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
