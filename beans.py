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
if not m or not n:
    print('NO')
else:
    beans = find_k(arr, n, m)
    if not beans is None:
        print(beans)


