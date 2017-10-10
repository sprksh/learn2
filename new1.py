nm = input()
n, m  = int(nm.split()[0]), int(nm.split()[1])

lon  = []
new_l = []

for j in range(m):
    lon.append([])

for i in range(n):
    s = input()
    for j in range(m):
        try:
            lon[j].append(s[j])
        except Exception:
            lon[j].append(' ')

for j in range(m):
    new_l += lon[j]

new_s = ''.join(new_l)

import re

pattern = '[!@ #$%&]'
gs = re.sub(pattern, ' ', new_s)

print(gs)


temp = arr[-1]
for i in reversed(list(range(1, n))):
    if arr[i-1] > temp:
        if not i == 1:
            arr[i] = arr[i-1]
        else:
            arr[1] = arr[0]
            arr[0] = temp
            break
    else:
        arr[i] = temp
        break
print(' '.join([str(i) for i in arr]))

x = arr[n-1]                                                 
for i in range(n-2):
    if arr[n-i-2]>x:
        arr[n-i-1]= arr[n-i-2]
        print(*arr, sep=' ')
    else:
        arr[n-i-1] = x
        print(*arr, sep=' ') 
        break
if arr[1] > x:
    if arr[0] >x:
        arr[1] = arr[0]
        print(*arr, sep=' ')
        arr[0]=x
        print(*arr, sep=' ')
    else:
        arr[1] = x
        print(*arr, sep=' ')

2 3 4 5 6 7 8 9 10 10
2 3 4 5 6 7 8 9 9 10
2 3 4 5 6 7 8 8 9 10
2 3 4 5 6 7 7 8 9 10
2 3 4 5 6 6 7 8 9 10
2 3 4 5 5 6 7 8 9 10
2 3 4 4 5 6 7 8 9 10
2 3 3 4 5 6 7 8 9 10
2 2 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

2 3 4 5 6 7 8 9 10 10
2 3 4 5 6 7 8 9 9 10
2 3 4 5 6 7 8 8 9 10
2 3 4 5 6 7 7 8 9 10
2 3 4 5 6 6 7 8 9 10
2 3 4 5 5 6 7 8 9 10
2 3 4 4 5 6 7 8 9 10
2 3 3 4 5 6 7 8 9 10
1 2 3 4 5 6 7 8 9 10

while i < n:
    if tl:
        print('cool', i)
        if x[i+1] > tl[-1]:
            for j in reversed(list(range(i+2*k))):
                if x[j] <= tl[-1] + 2*k:
                    tl.append(x[j+1])
                    last_x = tl[-1]
                    break
        i = i + k
    else:
        if x[-1] - x[0] < k:
            tl.append(x[0])
        else:
            for j in range(0, n):
                if x[j] - x[0] > k:
                    tl.append(x[j-1])
                    last_x = tl[-1]
                    i = j
                    break
                  