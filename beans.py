def find_k(arr, n, m):
    rem = n
    beans = 0
    while rem > 0:
        if rem < arr[0]:
            print('NO')
            return None
        for i in range(1, m+1):
            if arr[m-i] <= rem:
                beans += int(rem/arr[m-i])
                rem = rem % arr[m-i]
                if rem == 0:
                    return beans
            

    n, m = [int(t) for t in input().strip().split()]
    arr = [int(i) for i in input().strip().split()]
    arr.sort()
    beans = find_k(arr, n, m)
    if beans:
        print(beans)
    else:
        print('NO')


q = int(input())

def minC(arr, m, n):

    if (n == 0): 
        return 0
 
    res = 100000
 
    for i in range(m):
        if arr[i] <= n:
            sub_res = minC(arr, m, n-arr[i])
 
            if sub_res != 100000 and sub_res < res-1:
                res = sub_res + 1
    return res
        
   
for j in range(q):
    n, m = [int(t) for t in input().strip().split()]
    arr = [int(i) for i in input().strip().split()]
    arr = sorted(arr, reverse=True)
    beans = minC(arr, m, n)
    if beans:
        print(beans)
    else:
        print('NO')