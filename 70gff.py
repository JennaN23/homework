import gzip
import json
import re
import sys

# 70gff.py

# Write a program that converts genes in gff into JSON
# Use the E. coli genome gff
# Your code should mimic the output below

genes = []

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp:
		if line.startswith('NC_'):
			f = line.split()
			if f[2] != 'gene': continue
			#print(line)
			pat1 = '\;Name=(\w+)'
			match = re.search(pat1, line)
			if match:
				gene = match.group(1)
				#print(line, gene)
			genes.append({"gene": gene, "beg": f[3], "end": f[4], "strand": f[6]})

print(json.dumps(genes, indent=4))

"""
python3 70gff.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.gff.gz
[
    {
        "gene": "thrL",
        "beg": 190,
        "end": 255,
        "strand": "+"
    },
    {
        "gene": "thrA",
        "beg": 337,
        "end": 2799,
        "strand": "+"
    },
...
"""
