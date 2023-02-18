import gzip
import mcb185
import sys

# 41transmembrane.py

# Write a program that predicts which proteins in a proteome are transmembrane

# Transmembrane proteins are characterized by having
#    1. a hydrophobic signal peptide near the N-terminus
#    2. other hydrophobic regions to cross the plasma membrane

# Both the signal peptide and the transmembrane domains are alpha-helices
# Therefore, they do not contain Proline

# Hydrophobicity can be measured by Kyte-Dolittle
#	https://en.wikipedia.org/wiki/Hydrophilicity_plot

# For our purposes:
#	Signal peptide is 8 aa long, KD > 2.5, first 30 aa
#	Hydrophobic region is 11 aa long, KD > 2.0, after 30 aa

# Hint: copy mcb185.py to your homework repo and import that
# Hint: create a function for KD calculation
# Hint: create a function for hydrophobic alpha-helix
# Hint: use the same function for both signal peptide and transmembrane

def kd(seq, ws, start, end):
	aas = ['I', 'V', 'L', 'F', 'C', 'M', 'A', 'G', 'T', 'S', 'W', 'Y', 'P', 'H', 'E', 'Q', 'D', 'N','K', 'R']
	hyd = [4.5, 4.2, 3.8, 2.8, 2.5, 1.9, 1.8, -0.4, -0.7, -0.8, -0.9, -1.3, -1.6, -3.2, -3.5, -3.5, -3.5, -3.5, -3.9, -4.5]
	max_kd = 0
	kds  = []
	nseq = seq[start:end]
	for i in range(len(nseq) - ws + 1):
		kd = 0
		w  = nseq[i:i + ws]
		for aa in w:
			if aa in aas: 
				h  = hyd[aas.index(aa)]
				kd += h
		#print(w, kd)
		kds.append(kd)
		max_kd = max(kds)
	return max_kd
			#avg_kd = kd/len
			#if avg_kd > max_kd: max_kd = avg_kd
			#print(max_kd)
	#return avg_kd
		
def hydrophobic(seq, kd, t):
	if 'P' in seq or kd < t: return False
	else:                    return True

for name, seq in mcb185.read_fasta(sys.argv[1]):
	#print('sp')
	sp_kd  = kd(seq, 8, 0, 30)
	#print('hr')
	hr_kd  = kd(seq, 11, 30, len(seq) - 1)
	sp_hyd = hydrophobic(seq, sp_kd, 2.5)
	hr_hyd = hydrophobic(seq, hr_kd, 2.0)
	#print(sp_kd, hr_kd, sp_hyd, hr_hyd)
	if sp_hyd and hr_hyd: print(name)
	
"""
python3 41transmembrane.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
NP_414560.1 Na(+):H(+) antiporter NhaA [Escherichia coli str. K-12 substr. MG1655]
NP_414568.1 lipoprotein signal peptidase [Escherichia coli str. K-12 substr. MG1655]
NP_414582.1 L-carnitine:gamma-butyrobetaine antiporter [Escherichia coli str. K-12 substr. MG1655]
NP_414607.1 DedA family protein YabI [Escherichia coli str. K-12 substr. MG1655]
NP_414609.1 thiamine ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414653.1 protein AmpE [Escherichia coli str. K-12 substr. MG1655]
NP_414666.1 quinoprotein glucose dehydrogenase [Escherichia coli str. K-12 substr. MG1655]
NP_414695.1 iron(III) hydroxamate ABC transporter membrane subunit [Escherichia coli str. K-12 substr. MG1655]
NP_414699.1 PF03458 family protein YadS [Escherichia coli str. K-12 substr. MG1655]
NP_414717.2 CDP-diglyceride synthetase [Escherichia coli str. K-12 substr. MG1655]
...
"""
