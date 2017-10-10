n, k = [int(i) for i in input().strip().split()]
arr = [int(i) for i in input().strip().split()]

def KswapPermutation(arr, n, k):
    pos = {}
    for i in range(n):
        pos[arr[i]] = i
 
    for i in range(n):
        if k == 0:
            break
        if (arr[i] == n-i):
            continue
        temp = pos[n-i]
        pos[arr[i]] = pos[n-i]
        pos[n-i] = i
        arr[temp], arr[i] = arr[i], arr[temp]
 
        k = k-1
        
KswapPermutation(arr, n, k)
print(*arr, sep=' ')

----------------------------------------------

n, k = [int(i) for i in input().strip().split()]
arr = [int(i) for i in input().strip().split()]

i = 0

while k > 0 and i < n-1:
    j = arr.index(n-i)
    if not j == i:
        arr[j] = arr[i]
        arr[i] = n-i
    k -= 1
    i += 1

print(*arr, sep=' ')

***********************************************

N, k = map(int,raw_input().split())
C = map(int,raw_input().split())
cost =0
if N<k:
    print sum(C[0:N])
else:
    w = sorted(C,reverse=True)
    i = 0
    while(len(w)>0):
        cost += (i+1)*sum(w[0:k])
        i+=1
        w = w[k:N]
    print cost


def getMinimumCost(n, k, c):
    c.sort()
    dic = {}
    f = int(n/k)
    fl = [f for i in range(k)]
    r = n%k
    
    for i in range(1, f+1):
        dic[i] = k
    if r:
        dic[f+1] = r
    su = 0
    dicc = list(sorted(dic.items(), reverse=True))
    
    i = 0
    for k in dicc:
        for o in range(1, k[-1]+1):
            su += k[0] * c[i]
            i+=1
    return su
        
n, k = input().strip().split(' ')
n, k = [int(n), int(k)]
c = list(map(int, input().strip().split(' ')))
minimumCost = getMinimumCost(n, k, c)
print(minimumCost)