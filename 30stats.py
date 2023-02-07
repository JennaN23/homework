import sys

# 30stats.py

# Write a program that computes typical stats
# Count, Min, Max, Mean, Std. Dev, Median

# Hint: use sys.argv to get the values from the command line

# Note: you are not allowed to import any library except sys

count = len(sys.argv[1:])
sum   = 0
stdv  = 0
lst   = []

for num in sys.argv[1:]:
	lst.append(int(num))
	sum += int(num)
	
lst.sort()
mean  = sum/count
med   = lst[int(count/2)]

# std. dev
for num in lst:
	stdv += ((num - mean)**2)	
	
print(f'Count: {count}')
print(f'Minimum: {min(lst):.1f}')
print(f'Maximum: {max(lst):.1f}')
print(f'Mean: {mean:.3f}')
print(f'Std. dev: {(stdv/count)**0.5:.3f}')
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
