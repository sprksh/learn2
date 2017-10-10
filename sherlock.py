n = int(input().strip())

lis = [int(i) for i in input().strip().split()]

p, q = [int(i) for i in input().strip().split()]

piq = list(range(p, q+1))
dic = []
for i in range(p, q+1):
    u = min([abs(i-j) for j in lis])
    dic.append(u)
k = piq[dic.index(max(dic))]
print(k)