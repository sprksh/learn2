# fibonacci

# a, b = 0, 1
# for i in range(1, 10):
# 	val =  a + b
# 	a = b
# 	b = val
# 	print(val)


# sigma 2^n

sum = 0
for i in range(1, 20):
	p = 1/i
	print(p)
	val = 2.0**p
	sum += val
	print(sum)

import sys
print(sys.version)