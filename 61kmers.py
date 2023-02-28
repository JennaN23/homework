import argparse
import mcb185

# 61kmers.py

# Make a program that reports the kmer counts for a fasta file
# Your program should take 2 arguments:
#    1. The file name
#    2. The size of k

# Hint: use argparse
# Hint: use mcb185.read_fasta()

def kmer_count(seq, k):
	for i in range(len(seq) - k + 1):
		kmer = seq[i:i + k]
		if kmer not in kmers: kmers[kmer] = 0
		kmers[kmer] += 1

# setup
parser = argparse.ArgumentParser(description='Brief description of program.')

# positional arguments (always required)
parser.add_argument('file', type=str, metavar='<file>', help='some file')

# optional arguments with default parameters
parser.add_argument('-k', required=False, type=int, default=5,
	metavar='<int>', help='kmer size [%(default)s]')

# finalization
arg = parser.parse_args()

"""
# testing
print(arg.file)
print(arg.k)
"""
kmers = {}

for name, seq in mcb185.read_fasta(arg.file):
	kmer_count(seq, arg.k)
	
for key, val in sorted(kmers.items(), key=lambda item: item[0]): 
	print(key, val)

"""
python3 60kmers.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 2
AA 338006
AC 256773
AG 238013
AT 309950
CA 325327
CC 271821
CG 346793
CT 236149
GA 267384
GC 384102
GG 270252
GT 255699
TA 212024
TC 267395
TG 322379
TT 339584
"""
