# Prog 1

# array = []
# n = len(array)

# def sums(arr):


# def find_min(ar, n):
# 	ar.sort()
# 	if ar[0] != 1:
# 		return 1
# 	for i in range(sum(ar) + 2):
# 		for j in range(1, n):
# 			temp_ar = ar[:j]
# 			if sum(temp_ar) > i:
# 				break
# 			if sum(temp_ar) == i:
# 				retur

def findS(arr, n):
    res = 1
    i = 0
    if i <n and arr[i]<= res:
        i += 1
        res += arr[i]
    return res
