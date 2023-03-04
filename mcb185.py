# mcb185.py

import gzip
import math
import sys

def read_fasta(filename):

	if   filename == '-':          fp = sys.stdin
	elif filename.endswith('.gz'): fp = gzip.open(filename, 'rt')
	else:                          fp = open(filename)

	name = None
	seqs = []

	while True:
		line = fp.readline()
		if line == '': break
		line = line.rstrip()
		if line.startswith('>'):
			if len(seqs) > 0:
				yield(name, ''.join(seqs))
				name = line[1:]
				seqs = []
			else:
				name = line[1:]
		else:
			seqs.append(line)

	yield(name, ''.join(seqs))
	fp.close()

# def other functions...
		
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
	
def translate(dna, frame=0):
	aaseq = ''
	dna   = dna.upper()
	gcode = {
	'AAA' : 'K',	'AAC' : 'N',	'AAG' : 'K',	'AAT' : 'N',
	'ACA' : 'T',	'ACC' : 'T',	'ACG' : 'T',	'ACT' : 'T',
	'AGA' : 'R',	'AGC' : 'S',	'AGG' : 'R',	'AGT' : 'S',
	'ATA' : 'I',	'ATC' : 'I',	'ATG' : 'M',	'ATT' : 'I',
	'CAA' : 'Q',	'CAC' : 'H',	'CAG' : 'Q',	'CAT' : 'H',
	'CCA' : 'P',	'CCC' : 'P',	'CCG' : 'P',	'CCT' : 'P',
	'CGA' : 'R',	'CGC' : 'R',	'CGG' : 'R',	'CGT' : 'R',
	'CTA' : 'L',	'CTC' : 'L',	'CTG' : 'L',	'CTT' : 'L',
	'GAA' : 'E',	'GAC' : 'D',	'GAG' : 'E',	'GAT' : 'D',
	'GCA' : 'A',	'GCC' : 'A',	'GCG' : 'A',	'GCT' : 'A',
	'GGA' : 'G',	'GGC' : 'G',	'GGG' : 'G',	'GGT' : 'G',
	'GTA' : 'V',	'GTC' : 'V',	'GTG' : 'V',	'GTT' : 'V',
	'TAA' : '*',	'TAC' : 'Y',	'TAG' : '*',	'TAT' : 'Y',
	'TCA' : 'S',	'TCC' : 'S',	'TCG' : 'S',	'TCT' : 'S',
	'TGA' : '*',	'TGC' : 'C',	'TGG' : 'W',	'TGT' : 'C',
	'TTA' : 'L',	'TTC' : 'F',	'TTG' : 'L',	'TTT' : 'F',
}

	for i in range(frame, len(dna) - 2 - frame, 3):
			codon = dna[i:i + 3]
			if codon not in gcode: aaseq += 'X'
			else: 
				aaseq += gcode[codon]
				if gcode[codon] == '*': 
					#print(aaseq)
					break
	return aaseq
		
def rc(seq):
	revc = ''
	comp = {'A': 'T', 'C': 'G', 'G': 'C', 'T': 'A'}
	rseq = seq[::-1]
	for nt in rseq:
		revc += comp[nt]
	return revc
		
		
