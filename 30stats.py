import sys

# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

c    = len(sys.argv[1:])
sum  = 0
stdv = 0
lst  = []

for val in sys.argv[1:]:
	try:
		p = float(val)
	except:
		raise ValueError(f'Cannot convert {val} to float')

for num in sys.argv[1:]:
	lst.append(float(num))
	sum += float(num)
	
lst.sort()
mean  = sum/c
med   = lst[int(c/2)]

# std. dev
for num in lst:
	stdv += ((num - mean)**2)	
print(f'Count: {c}')
print(f'Minimum: {min(lst):.1f}')
print(f'Maximum: {max(lst):.1f}')
print(f'Mean: {mean:.3f}')
print(f'Std. dev: {(stdv/c)**0.5:.3f}')
print(f'Median: {med:.3f}') 

"""
python3 30stats.py 3 1 4 1 5
Count: 5
Minimum: 1.0
Maximum: 5.0
Mean: 2.800
Std. dev: 1.600
Median 3.000
"""
