import gzip
import sys

# 40aacomp.py

# Make a program that reports the amino acid composition in a file of proteins

# Note: you are not allowed to import any libraries except gzip and sys

# Hint: gzip.open(sys.argv[1], 'rt')

# Variation: use a list

aas = ['A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V','W', 'Y']
tot = 0
c= [0]*20

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		line = line.rstrip()
		if line[0] == '>': continue
		for aa in line:
			if aa in aas: 
				tot += 1
				c[aas.index(aa)] += 1

for i in range(20):
	print(f'{aas[i]} {c[i]} {c[i]/tot:.4f}')


"""
# Variation: use 20 named variables

a = 0
c = 0
d = 0
e = 0
f = 0
g = 0
h = 0
i = 0
k = 0
l = 0
m = 0
n = 0
p = 0
q = 0
r = 0
s = 0
t = 0
v = 0
w = 0
y = 0
tot = 0

with gzip.open(sys.argv[1], 'rt') as fp:
	for line in fp.readlines():
		if line[0] == '>': continue
		for aa in line:
			if   aa == 'A': a += 1
			elif aa == 'C': c += 1
			elif aa == 'D': d += 1
			elif aa == 'E': e += 1
			elif aa == 'F': f += 1
			elif aa == 'G': g += 1
			elif aa == 'H': h += 1
			elif aa == 'I': i += 1
			elif aa == 'K': k += 1
			elif aa == 'L': l += 1
			elif aa == 'M': m += 1
			elif aa == 'N': n += 1
			elif aa == 'P': p += 1
			elif aa == 'Q': q += 1
			elif aa == 'R': r += 1
			elif aa == 'S': s += 1
			elif aa == 'T': t += 1
			elif aa == 'V': v += 1
			elif aa == 'W': w += 1
			elif aa == 'Y': y += 1
			else: continue
			tot += 1
print(f'A {a} {a/tot:.4f}')
print(f'C {c} {c/tot:.4f}')
print(f'D {d} {d/tot:.4f}')
print(f'E {e} {e/tot:.4f}')
print(f'F {f} {f/tot:.4f}')
print(f'G {g} {g/tot:.4f}')
print(f'H {h} {h/tot:.4f}')
print(f'I {i} {i/tot:.4f}')
print(f'K {k} {k/tot:.4f}')
print(f'L {l} {l/tot:.4f}')
print(f'M {m} {m/tot:.4f}')
print(f'N {n} {n/tot:.4f}')
print(f'P {p} {p/tot:.4f}')
print(f'Q {q} {q/tot:.4f}')
print(f'R {r} {r/tot:.4f}')
print(f'S {s} {s/tot:.4f}')
print(f'T {t} {t/tot:.4f}')
print(f'V {v} {v/tot:.4f}')
print(f'W {w} {w/tot:.4f}')
print(f'Y {y} {y/tot:.4f}')
"""


"""
python3 40aacomp.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_protein.faa.gz
A 126893 0.0954
C 15468 0.0116
D 68213 0.0513
E 76890 0.0578
F 51796 0.0389
G 97830 0.0736
H 30144 0.0227
I 79950 0.0601
K 58574 0.0440
L 142379 0.1071
M 37657 0.0283
N 51896 0.0390
P 59034 0.0444
Q 59178 0.0445
R 73620 0.0554
S 76865 0.0578
T 71428 0.0537
V 94237 0.0709
W 20297 0.0153
Y 37628 0.0283
"""
