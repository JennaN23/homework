import math
import sys

# 31entropy.py

# Write a Shannon entropy calculator: H = -sum(pi * log(pi))
# The values should come from the command line
# Store the values in a new list

# Note: make sure the command line values contain numbers
# Note: make sure the probabilities sum to 1.0
# Note: import math and use the math.log2()

# Hint: try breaking your program with erroneous input

h   = 0
lst = []

for val in sys.argv[1:]:
	try: 
		lst.append(float(val))
	except:
		raise ValueError(f'Cannot convert {val} to float')
		
assert(math.isclose(sum(lst), 1.0))

for i in lst:
	h += (i * math.log2(i))
print(f'{-h:.3f}')

"""
python3 31entropy.py 0.1 0.2 0.3 0.4
1.846
"""
